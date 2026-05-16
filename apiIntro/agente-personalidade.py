from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat

#carregar a chave de API
load_dotenv()

#crio o modelo de IA
agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    description="Você é uma florista",
    markdown=True
)

while True:
    pergunta = input("Digite a sua pergunta: ")

   # if pergunta.lower() == "sair" or pergunta.lower() == "exit":
    if pergunta.lower() in ['exit', 'sair', 'quit', 'cancelar', 'finalizar', 'bye', 'vou dormir']:
       print("Saindo...Fique a vontade para fazer mais perguntas😒")
       break
    else:
       agente.print_response(pergunta)

