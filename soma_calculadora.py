print("-" * 50)
print("\t ****************** Calculadora de soma ******************* ")
print("-" * 50)

firstNumber = int(input("Digite o primeiro numero: "))
secondNumber = int(input("Digite o segundo numero: "))

if not type(firstNumber) is int and not type(secondNumber) is int:
    Exception("Dado invalido")

soma = firstNumber + secondNumber

print("-" * 50)
print("\t ****************** Resultado da soma ******************* ")
print("-" * 50)

print(f" A soma é: {soma}")
print("-" * 50)
