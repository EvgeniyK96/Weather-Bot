import os
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

bot_token = config['Bot']['TOKEN']
weather_api_key = config['Weather']['API_KEY']

host = config['Database']['HOST']
port = config['Database']['PORT']
database = config['Database']['DATABASE']
user = config['Database']['USER']
password = config['Database']['PASSWORD']