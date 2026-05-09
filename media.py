print("\t ****************** Calcula a media ******************* ")

notaUm     = float(input("Qual a primeira nota do aluno? "))
notaDois   = float(input("Qual a segunda nota do aluno? "))
notaTres   = float(input("Qual a terceira nota do aluno? "))
notaQuatro = float(input("Qual a quarta nota do aluno? "))

media = (notaUm + notaDois + notaTres + notaQuatro) / 2
print(f"A media é {media}")

print("\t ****************** Conclusão ******************* ")

if media >= 6:
    print("Aprovado, Parabéns!!!!!")
else:
    print("Reprovado, Tente Novamente 😒")
