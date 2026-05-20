# import ============================================
import json
import telebot
import requests
from telebot import types
from weather import get_weather

from config import bot_token, weather_api_key

#Initialization=======================================



bot = telebot.TeleBot(token=bot_token, parse_mode='HTML')

def register_buttons():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Зарегестрироваться", request_contact=True)
    markup.add(btn)
    return markup

def get_location():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton("Поделится городом", request_location=True)
    markup.add(btn)
    return markup


@bot.message_handler(commands=['start'])
def send_welcome(message: types.Message):
    
    bot.send_animation(
        message.chat.id, 
        "CgACAgIAAxkDAAOFagyG6bBK_oEsR5xWJcfPpQksN2kAAkCeAAJKxmBISpevDZO12SE7BA",
        caption=f"Привет, {message.from_user.first_name}! Напиши название города, и я расскажу тебе погоду там!"
    )



@bot.message_handler(content_types=['text'])
def handle_text(message: types.Message):
    pass



#start=============================================

if __name__ == '__main__':
    print('Bot is running...')
    bot.polling(none_stop=True)