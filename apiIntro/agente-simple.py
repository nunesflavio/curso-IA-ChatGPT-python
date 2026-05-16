from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.openai import OpenAIChat
#Todos agentes necessitam ca chave de API, e a função LOAD_DOTENV faz a leitura do arquivo no .env
load_dotenv()

agente = Agent(
    #aqui define modelo do agente
    model=OpenAIChat(id="gpt-4o-mini"),
    markdown=True
)

agente.print_response("Qual melhor sistema operacional Windows ou Linux?")
