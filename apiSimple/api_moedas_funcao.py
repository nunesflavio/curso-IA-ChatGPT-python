import requests

#comando para criar funcao DEF
def get_moedas():

    url = "https://api.exchangerate-api.com/v4/latest/BRL"
    try:

        data = requests.get(url).json()
        dolarUSD = data["rates"]["USD"]
        dolar = 1 / dolarUSD

        euroRate = data["rates"]["EUR"]
        euro = 1 / euroRate

        return f"{dolar:.2f} BRL = 1 USD"

    except:
        return("Não foi possivel fazer a conversao de valores")

print(get_moedas())

