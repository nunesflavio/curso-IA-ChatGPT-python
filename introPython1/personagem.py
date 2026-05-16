print("-" * 50)
print("\t ****************** Digite sobre seu personagem ******************* ")
print("-" * 50)

personagemClasse = ["mago", "guerreiro", "Elfo", "fada"]
skinPersonagem = ["gratis", "plus", "pro"]

nome = input("Digite o nome do personagem: ")
personagem = input("Digite a classe do personagem: [mago, guerreiro, Elfo, fada] ")

if personagem in personagemClasse:
    skin = input("Digite o nome do skin: (gratis, plus ou pro) ")

    if skin in skinPersonagem:
        print(f"nome do personagem: {nome} , a classe do personagem: {personagem}, skin: {skin}")
