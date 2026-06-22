# import ============================================
import json
import telebot
import requests
from telebot import types

from weather import get_weather
from database import user_get, user_create, user_update
from config import bot_token
from utils import get_address

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
    user_id = message.from_user.id

    if user_get(user_id) is not None:
        bot.send_message(
            message.chat.id,
            text=(
            f"Добро пожаловать {message.from_user.full_name} в бот погоды!"
            "Для просмотра погоды, пожалуйста, нажмите кнопку 'Поделиться городом'."
            "Или напишите название города, чтобы узнать погоду."
            ),
            reply_markup=get_location()
        )

    else:
        bot.send_message(
            message.chat.id,
            text=(
            f"Добро пожаловать {message.from_user.full_name} в бот погоды!"
            "Для начала работы, пожалуйста, зарегистрируйтесь."
            "Для регистрации, пожалуйста, нажмите кнопку 'Зарегистрироваться'."
            ),
            reply_markup=register_buttons()
        )

    #     user_create(
    #         user_id=user_id,
    #         username=message.from_user.username,
    #         first_name=message.from_user.first_name,
    #         last_name=message.from_user.last_name,
    #         phone="No phone number",
    #         location="No location",
    #         city="No city"
    #     )
    


    # bot.send_animation(
    #     message.chat.id, 
    #     "CgACAgIAAxkDAAOFagyG6bBK_oEsR5xWJcfPpQksN2kAAkCeAAJKxmBISpevDZO12SE7BA",
    #     caption=f"Привет, {message.from_user.first_name}! Напиши название города, и я расскажу тебе погоду там!"
    # )

@bot.message_handler(content_types=['contact'])
def handle_contact(message: types.Message):
    user_id = message.from_user.id

    if user_get(user_id) is not None:
        bot.send_message(
            message.chat.id,
            text=f"Вы уже зарегистрированы в боте!",
            reply_markup=get_location()
        )
    else:
        user_id_from_contact = message.contact.user_id
        if user_id == user_id_from_contact:
            user_create(
                user_id=user_id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                phone=message.contact.phone_number,
                location="No location",
                city="No city"
            )
            bot.send_message(
                message.chat.id,
                text="Вы успешно зарегистрированы в боте!",
                reply_markup=get_location()
            )
        else:
            bot.send_message(
                message.chat.id,
                text="Вы не можете зарегистрироваться с другого номера телефона!",
                reply_markup=register_buttons()
            )


@bot.message_handler(content_types=['text'])
def handle_text(message: types.Message):
    user_id = message.from_user.id
    if user_get(user_id) is not None:
        city = message.text.lower().capitalize()
        weather = get_weather(city)
        bot.send_message(message.chat.id, text=weather, reply_markup=get_location())
    else:
        bot.send_message(
            message.chat.id,
            text=f"Вы не зарегистрированы в боте!",
            reply_markup=register_buttons()
        )


@bot.message_handler(content_types=['location'])
def handle_location(message: types.Message):
    user_id = message.from_user.id
    if user_get(user_id) is not None:
        latitude = message.location.latitude
        longitude = message.location.longitude
        address = get_address(latitude, longitude)
        city = address.split(",")[-3].strip()
        
        if address is not None:
            user_update(
                user_id=user_id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                location=address,
                city=city
            )
            bot.send_message(
                message.chat.id,
                text=get_weather(city),
                reply_markup=get_location()
            )
    else:
        bot.send_message(
            message.chat.id,
            text=f"Вы не зарегистрированы в боте!",
            reply_markup=register_buttons()
        )



#start=============================================

if __name__ == '__main__':
    from database import init_db
    init_db() 
    print('Bot is running...')
    bot.polling(none_stop=True)