import streamlit as st

st.title("Secretaria SENAI Americana")
st.subheader("Conheça os nossos cursos")

st.write("I.A Genarativa, PowerBI, Empilhadeira, Excel, Eletrecista Instalador")
st.markdown("**Atenção**: Verifique se existem vagas disponiveis.")

nome = st.text_input("Digite o seu nome")
idade = st.text_input("Digite sua idade", min_value=16, max_value=99)
cursoEscolhido = st.selectbox("Cursos disponiveis",["I.A Generativa", "PowerBI", "Empilhadeira", "Excel",
                                                    "Eletrecista"])
aceitaTermos= st.checkbox("Ao clicar aqui voce aceita termos e condições")

if st.button("Enviar resposta"):
    if nome and idade and cursoEscolhido and aceitaTermos:
        st.success(f"Ola {nome}, curso escolhido: {cursoEscolhido} ")

    else:
        st.error("Dados incorretos")