import requests as rq

try:
    cep = input("Digite o seu CEP: ")

    url = f"https://viacep.com.br/ws/{cep}/json/"

    data = rq.get(url).json()

    # print(data)

    print(f"Você mora na rua: {data["logradouro"]}, e no bairro: {data["bairro"]}, na cidade: {data['localidade']}, "
          f"e estado: {data['uf']}")

except:
    print("Ocorreu um erro!!!!!!")

