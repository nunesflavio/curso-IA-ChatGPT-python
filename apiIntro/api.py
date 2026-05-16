#instalar bibliotecas - pip instalador do python
#segundo passo - importar ao codigo requests

import requests

#Recebe os dados digitados pelo usuario
nome     = input("Digite o nome da pessoa: ")
email    = input("Digite o email da pessoa: ")
telefone = input("Digite o telefone da pessoa: ")
cepEnter = input("Digite o CEP: ")

try:
    #O 'f', para conseguir inserir uma variavel no link
    url = f"https://viacep.com.br/ws/{cepEnter}/json/"

    dados = requests.get(url).json()

    print(f"Bem vindo ao Mercado Livre {nome}! O seu email é: {email}. Seu telefone é: {telefone}."
          f"Você mora na rua {dados['logradouro']} e na cidade {dados['localidade']}")

except ValueError:
    print("Erro ao ler o CEP")
