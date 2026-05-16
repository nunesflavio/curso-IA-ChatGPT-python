"""
=============================================================================
  EXERCÍCIO 3A: [Some todos os números pares de 1 a 50 - Intro Python]

=============================================================================
"""

def main():

    print("------------------------------Iniciando exercício--------------------------------...")

    soma = 0
    for numero in range(1, 51):
        if numero % 2 == 0:  # Verifica se o número é par
            soma += numero
    print(soma)

#  É uma boa prática de Python para garantir que o código só execute quando o 'script' for rodado diretamente, e não
#  quando for importado como módulo.
if __name__ == "__main__":
    main()