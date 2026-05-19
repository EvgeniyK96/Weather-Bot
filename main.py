# import ============================================
import json
import telebot
import requests
from telebot import types

from config import bot_token, weather_api_key

#Initialization=======================================



bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome(message: types.Message):
    # with open('data.json', 'w') as f:
    #     json.dump(message.json, f, ensure_ascii=False, indent=4)

    bot.send_message(message.chat.id, "Привет! Введите название города, чтобы узнать погоду!")

@bot.message_handler(content_types=['text'])
def handle_text(message: types.Message):
    
    city = message.text
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_api_key}&units=metric&lang=ru"
    
    response = requests.get(url)
    data = response.json()
    with open('weather.json', 'w') as f:
         json.dump(data, f, ensure_ascii=False, indent=4)

    if data["cod"] == 200:
        city_name = data["name"]
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        
        result_message = (
            f"📍 Погода в городе {city_name}:\n"
            f"🌡 Температура: {temp} °C\n"
            f"☁️ На улице: {description.capitalize()}\n"
            f"💧 Влажность: {humidity} %\n"
            f"💨 Ветер: {wind_speed} м/с"
        )
        bot.send_message(message.chat.id, result_message)
    else:
        bot.send_message(message.chat.id, "Город не найден. Проверьте правильность написания!")


@bot.message_handler(content_types=['photo'])
def handle_image(message: types.Message):
    bot.send_photo(message.chat.id, message.photo[-1].file_id, caption="Вы отправили фото!")



#start=============================================

if __name__ == '__main__':
    print('Bot is running...')
    bot.polling(none_stop=True)