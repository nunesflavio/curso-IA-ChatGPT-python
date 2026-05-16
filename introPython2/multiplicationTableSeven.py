"""
=============================================================================
  EXERCÍCIO 3B: [Mostre a tabuada do 7 (de 1 a 10) - Intro Python]

=============================================================================
"""

def main():

    number = 1
    while number <= 10:

        sevenTable = number * 7

        print(f"{number} X 7 = {sevenTable}")
        number += 1

#  É uma boa prática de Python para garantir que o código só execute quando o 'script' for rodado diretamente, e não
#  quando for importado como módulo.
if __name__ == "__main__":
     main()