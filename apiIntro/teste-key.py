from dotenv import load_dotenv

load_dotenv()

key = load_dotenv()

if key:
    print(f"A chave foi carregada com sucesso. 🐍")
else:
    print("Chave com erro de leitura😒😒😒")