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
    # cursor.execute(f"insert into users (user_id, username, first_name, last_name, phone, location, city) values (%s, %s, %s, %s, %s, %s, %s)",
    #             (
    #                 134456789,
    #                 'fbdfbf',
    #                 'Edbfdb',
    #                 'Kurdfbd',
    #                 '+7734567890',
    #                 '55.7558, 37.6173',
    #                 'Astana'
    #             ))
    # db_config.commit()

    # city = "Almaty"
    # cursor.execute("SELECT * FROM users WHERE city = %s", (city,))
    # users = cursor.fetchall()
    # print(users)

    # cursor.execute("DELETE FROM users")
    # db_config.commit()
    
