import requests
from config import weather_api_key

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric&lang=ru"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        name = data["name"]
        country = data["sys"]["country"]
        description = data["weather"][0]["description"].capitalize()
        temp = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind_speed = data["wind"]["speed"]
        visibility = data["visibility"] // 1000  # в км
        clouds = data["clouds"]["all"]
        
        return (
            f"<b>🌍 {name}, {country} - {description}</b>\n"
            f"<blockquote>🌡  Температура:   {temp:+.1f}°C\n"
            f"🤔 Ощущается:    {feels_like:+.1f}°C\n"
            f"💧 Влажность:     {humidity}%\n"
            f"🧭 Давление:      {pressure} гПа\n"
            f"💨 Ветер:         {wind_speed} м/с\n"
            f"👁  Видимость:     {visibility} км\n"
            f"☁️  Облачность:    {clouds}%</blockquote>\n"
            )
    else:
        return f"Город {city} не найден. Пожалуйста, проверьте название и попробуйте снова."
