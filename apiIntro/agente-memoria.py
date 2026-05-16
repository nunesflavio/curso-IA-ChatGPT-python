from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.tavily import TavilyTools
from agno.db.sqlite import SqliteDb

#carregar a chave de API
load_dotenv()

bancoDados = SqliteDb(db_file="temp/registros.db")

#crio o modelo de IA
agente = Agent(
    model=OpenAIChat(id="gpt-4o-mini"),
    add_history_to_context=True,
    description="Você é um influenciador de rede social focado em celular",
    tools=[DuckDuckGoTools(),TavilyTools],
    session_id="086af293-b7d6-4ebf-9079-82cd3d837998",
    num_history_runs=7,
    db=bancoDados,
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
