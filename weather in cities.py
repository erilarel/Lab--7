import requests
import json


city_name = 'Москва'
key = 'fc0ec10564cb22f674993d3c28aff5c7'
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&lang=ru&units=metric&appid={key}"
data = requests.get(url).json()


temperature = data["main"]['temp']
temp_desc = data['weather'][0]['description']
pressure = round(data['main']['pressure'] * 0.7501)  # перевела из гектопаскалей в мм рт. столба
humidity = data['main']['humidity']

print(f"В городе {city_name} температура {temperature}°C, {temp_desc}\n"
    f"Влажность в городе составляет {humidity}%\n"
    f"Давление равно {pressure} мм. ртутного столба")