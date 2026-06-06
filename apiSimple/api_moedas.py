#API que realiza conversao entre moedas
import requests

url = "https://api.exchangerate-api.com/v4/latest/BRL"

data = requests.get(url).json()
dolarUSD = data["rates"]["USD"]
dolar = 1 / dolarUSD

print(f"{dolar:.2f} BRL = 1 USD")

euroRate = data["rates"]["EUR"]
euro = 1 / euroRate

print(f"{euro:.2f} BRL = 1 EUR")
