"""
=============================================================================
  EXERCÍCIO 2: [Nota do aluno, somente números - Intro Python]

  DESCRIÇÃO:
  [Receba uma nota (0–10) e retorne:
    >= 9.0 → "A" / >= 7.0 → "B" / >= 5.0 → "C" < 5.0 → "Reprovado"
  ]
=============================================================================
"""

def main():

    print("------------------------------Iniciando exercício--------------------------------...")

try:
    note = float(input('Digite a nota do aluno: '))

    if note >= 9.0 and note >= 10.0:
        print("A")
    elif note >= 7.0:
        print("B")
    elif note >= 5.0:
        print("C")
    elif note < 5.0:
        print("Reprovado")
except ValueError:
    print("Você não digitou um número válido.")

#  É uma boa prática de Python para garantir que o código só execute quando o 'script' for rodado diretamente, e não
#  quando for importado como módulo.
if __name__ == "__main__":
    main()