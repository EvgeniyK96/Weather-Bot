"""
create table users (
  id serial primary key,
  user_id bigint,
  username varchar(100) default 'No username',
  first_name varchar(255) default 'No first name',
  last_name varchar(255) default 'No last name',
  phone varchar(25) default 'No phone number',
  location varchar(255) default 'No location',
  city varchar(255) default 'No city'
)
"""

import os 
os.system("clear")

import psycopg2
from config import host, port, user, password, database

CONNECT = {
    'host': host,
    'port': port,
    'user': user,
    'password': password,
    'dbname': database
}

db_config = psycopg2.connect(**CONNECT)

# Учитель сказал: Пообщаться с GPT или Cloud и попрактиковаться в SQL запросах
with db_config.cursor() as cursor:
    cursor.execute("select * from users")
    users = cursor.fetchall()
    print(users)
