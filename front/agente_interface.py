import streamlit as st
from agno.models.openai import OpenAIChat
from agno.agent import Agent
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.wikipedia import WikipediaTools

#ler a chave da API
from dotenv import load_dotenv

load_dotenv()

#Tupla pois nao sera alterado os parametros do agente
agente = Agent(
    #model=OpenAIChat(id="gpt-4o-mini"),
    model=OpenAIChat(id="gpt-5.4"),
    description="Voce é um influenciador de redes sociais que posta sobre viagens",
    tools=[DuckDuckGoTools(),WikipediaTools()],
    markdown=True
)

st.title("Agente de I.A 🐍🐍 - ChatGpt")

pergunta = st.chat_input("O que quer falar?")

if pergunta:
    with st.chat_message("user"):
        st.markdown(pergunta)
    with st.chat_message("assistant"):
        with st.spinner("Agente pensando..."):
            resposta = agente.run(pergunta)
            st.markdown(resposta.content)