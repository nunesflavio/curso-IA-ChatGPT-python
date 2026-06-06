from datetime import datetime

import streamlit as st
import requests

from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools

#ler a chave da API
from dotenv import load_dotenv

load_dotenv()

#criando funções (habilidades/skills)
def get_moedas():

    url = "https://api.exchangerate-api.com/v4/latest/BRL"

    try:

        data = requests.get(url).json()

        timestamp = data["time_last_updated"]
        data_convertida = datetime.fromtimestamp(timestamp)

        rateDolar = 1 / data["rates"]["USD"]
        rateEuro = 1 / data["rates"]["EUR"]

        return f" 1 real equivale a {rateDolar} USR. 1 real equivale a {rateEuro}. Dados atualizados em: {data_convertida}"

    except:
        print("Problema na execução da cotação!!")

personalidade = st.sidebar.selectbox("Personalidade", ["Professor de Python", "Professor de História",
                                                       "Cientista maluco", "Procurador de conversão"])

descricao = {
    "Professor de Python": "Você  é um professor de Python que responde com exempls e contexto",
    "Professor de História": "Você é um professor de história que ensona de forma clara, simples e objetiva",
    "Cientista maluco": "Você é um cientista maluco que sempres está em busca de novas inovações e projetos",
    "Procurador de conversão": "Você é uma pessoa muito interessada em conversões de moedas"
}

agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description=descricao[personalidade],
    tools=[DuckDuckGoTools(),WikipediaTools()],
    markdown=True
)

if "mensagens" not in st.session_state:
    st.session_state.mensagem = []

for msg in st.session_state.mensagem:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


if st.sidebar.button("Limpar conversas"):
    st.session_state.mensagem = []
    st.rerun()

st.title("Sistema Multiagentes")
pergunta = st.chat_input("Pergunte ao Agente")

if pergunta:
    with st.chat_message("user"):
        st.markdown(pergunta)

    st.session_state.mensagem.append({"role": "user", "content": pergunta})

    with (st.chat_message("assistant")):
        with st.spinner("Agente pensando..."):

            contexto = ""

            if personalidade == "Procurador de conversão":

                if "dólar" in pergunta.lower() or "euro" in pergunta.lower() or "moedas" in pergunta.lower() or 'EURO' in pergunta or 'dolar' in pergunta.lower():

                    contexto = f"O valor atual de conversão de USD e EUR para BRL é {get_moedas()}"

                    resposta = agente.run(pergunta + contexto)
                    st.markdown(resposta.content)

            #else:
                #notMoeda = "Você não esta autorizado a ver sobre o assunto de conversões"
               # resposta = agente.run(pergunta + notMoeda)
                #st.markdown(resposta.content)

            st.session_state.mensagem.append({"role": "assistant", "content": resposta.content})
