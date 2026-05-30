import streamlit as st
from altair.vegalite.v6 import theme

fundo_css = """
<style>
    /* Altera o fundo principal da área de conteúdo */
    [data-testid="stAppViewContainer"] {
        background-color: #808000; 
    }

    /* Altera o fundo da barra lateral */
    [data-testid="stSidebar"] {
        background-color: #e9ecef;
    }
</style>
"""

st.markdown(fundo_css, unsafe_allow_html=True)

st.title("Bem vindo a Pizzaria DiPadre1")
st.subheader("Veja nossas promoções")

nome = st.text_input("Digite o seu nome")
bairro = st.text_input("Digite o bairro")
cidade = st.text_input("Digite a cidade")

sabores = st.selectbox("Sabores", ["Escolha um sabor","Calabresa", "Margherita", "Portuguesa", "Quatro Queijos"])

if st.button("Enviar Pesquisa"):
    if nome and bairro and cidade and sabores:
        st.success(f"Ola {nome}, bairro {bairro}, cidade {cidade}, sabores: {sabores}")
        st.balloons()
    else:
        st.error("Preencha todos os campos")
