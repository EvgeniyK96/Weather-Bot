import os
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

bot_token = config['Bot']['TOKEN']
weather_api_key = config['Weather']['API_KEY']

