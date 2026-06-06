import os
import requests

api_key = "75e02b395a4bdacbd4c4c21380c1adcc"
#api_key = os.environ.get("OPENWEATHER_API_KEY")
cidade = "Americana"

url = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={api_key}&units=metric&lang=pt"

data = requests.get(url).json()

temperaturaAtual = data["main"]["temp"]
umidadeAtual = data["main"]["humidity"]
weatherDescription = data["weather"][0]["description"]

print(temperaturaAtual)
print(umidadeAtual)
print(weatherDescription)
