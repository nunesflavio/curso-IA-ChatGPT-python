"""
=============================================================================
  EXERCÍCIO 1: [Qual ano de nascimento e idade - Intro Python]

  DESCRIÇÃO:
  [Peça nome e ano de nascimento. Calcule a idade aproximada (2026 - ano) e mostre uma mensagem formatada.]
=============================================================================
"""
from datetime import datetime

def main():

    print("------------------------------Iniciando exercício--------------------------------...")

    name      = input("Digite seu nome: ")
    yearBirth = input("Digite o seu ano de nascimento: ")

    yearToday = datetime.now().year
    ageNow    = yearToday - int(yearBirth)

    print(f"Seu nome é: {name}, seu ano de nascimento é: {yearBirth}")
    print(f"Sua idade é: {ageNow} anos")

#  É uma boa prática de Python para garantir que o código só execute quando o 'script' for rodado diretamente, e não
#  quando for importado como módulo.
if __name__ == "__main__":
    main()
