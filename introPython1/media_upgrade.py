listaNotas = []

print("-" * 50)
print("\t ****************** Bem vindo a I.A que calcula notas e média final ******************* ")

while True:

    notas = input("Digite a nota que deseja inserir (Digite 'sair' para sair) ")

    if notas.lower() == "sair":
        break
    else:
        listaNotas.append(float(notas)) #insere dados em uma lista

media = sum(listaNotas) / len(listaNotas)

print(f"Media final do aluno: {media}")

