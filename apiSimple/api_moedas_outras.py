import requests

#comando para criar funcao DEF
def get_moedas():

    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:

        data = requests.get(url).json()
        rateBrl     = data["rates"]["BRL"]
        rateEuro    = data["rates"]["EUR"]
        rateLibra   = data["rates"]["GBP"]
        ratePesoArg = data["rates"]["ARS"]

        return (f" 1 dolar equivale a {rateBrl} BRL. 1 dolar equivale a {rateEuro} EUR. 1 dolar equivale a {rateLibra} GBP "
                f"1 dolar equivale a {ratePesoArg} ARS")

    except:
        return "Não foi possivel fazer a conversao de valores"

print(get_moedas())
