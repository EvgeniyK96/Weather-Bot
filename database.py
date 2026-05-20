import psycopg2
from config import host, port, database, user, password

CONNECT = {
    'host': host,
    'port': port,
    'dbname': database,
    'user': user,
    'password': password
}

db_config = psycopg2.connect(**CONNECT)

def user_get_or_create( **kwargs):
    with db_config.cursor() as cursor:
        cursor.execute(f"select * from users where user_id = {kwargs.get('user_id')}")
        user = cursor.fetchone()
        if user is not None:
            return user
        else:
            cursor.execute(
                f"insert into users (user_id, username, first_name, last_name, phone, location, city) values (%s, %s, %s, %s, %s, %s, %s)",
                (
                    kwargs.get('user_id'),
                    kwargs.get('username'),
                    kwargs.get('first_name'),
                    kwargs.get('last_name'),
                    kwargs.get('phone'),
                    kwargs.get('location'),
                    kwargs.get('city')
                )
            )
            return None
