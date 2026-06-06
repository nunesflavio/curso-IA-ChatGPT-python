import requests

api_key = "75e02b395a4bdacbd4c4c21380c1adcc"
#api_key = os.environ.get("OPENWEATHER_API_KEY")
cidade = input("Digite o nome da cidade: ")

def get_clima():

    try:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt"

        data = requests.get(url).json()

        temperaturaAtual = data["main"]["temp"]
        umidadeAtual = data["main"]["humidity"]
        weatherDescription = data["weather"][0]["description"]

        return f"Temperatura: {temperaturaAtual}, umidade do ar: {umidadeAtual}, Clima está: {weatherDescription}"

    except:
        return "Algum dado invalido"

print(get_clima())
