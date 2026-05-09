import datetime

print("=" *70)
print("Coletor de dados do chatGpt 🦈")
print("=" *70)

nome        = input("Qual o seu nome? ") #input - recebe dados do teclado do usuario
email       = input("Qual o seu email? ")
city        = input("Qual a sua cidade? ")
estate      = input("Qual a sua estado? ")
country     = input("Qual a sua País? ")
ageNow      = input("Qual a sua idade? ")
ageFuture   = int(ageNow) + 1
yearNow   = datetime.date.today().year
birthYear       = yearNow - int(ageNow)

print(f"Ola {nome}, seu email é: {email}, reside na cidade: {city}, estado: {estate} e país: {country} "
      f" a sua idade é {ageNow}, no futuro terá: {ageFuture}. Ano nascimento: {birthYear}")
# f minusculo antes das aspas permite que eu trabalhe com variaveis na frase. As chaves {} servem para eu
# chamar uma variavel para dentro da frase


