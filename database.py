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

# def user_get_or_create( **kwargs):
#     with db_config.cursor() as cursor:
#         cursor.execute(f"select * from users where user_id = {kwargs.get('user_id')}")
#         user = cursor.fetchone()
#         if user is not None:
#             return user
#         else:
#             cursor.execute(
#                 f"insert into users (user_id, username, first_name, last_name, phone, location, city) values (%s, %s, %s, %s, %s, %s, %s)",
#                 (
#                     kwargs.get('user_id'),
#                     kwargs.get('username'),
#                     kwargs.get('first_name'),
#                     kwargs.get('last_name'),
#                     kwargs.get('phone'),
#                     kwargs.get('location'),
#                     kwargs.get('city')
#                 )
#             )
#             return None


def user_get(user_id):
    with db_config.cursor() as cursor:
        cursor.execute(f"select * from users where user_id = {user_id}")
        user = cursor.fetchone()
        return user
    
def user_create(**kwargs):
    try:
        with db_config.cursor() as cursor:
            cursor.execute(
                f"insert into users (user_id, username, first_name, last_name, phone, location, city) values (%s, %s, %s, %s, %s, %s, %s)",
                (kwargs.get("user_id"), kwargs.get("username"), kwargs.get("first_name"), kwargs.get("last_name"), kwargs.get("phone"), kwargs.get("location"), kwargs.get("city"))
            )
            db_config.commit()
    except Exception as e:
        print(e)
        return False
    else:
        return True

def user_update(**kwargs):
    try:
        with db_config.cursor() as cursor:
            cursor.execute(
                f"update users set username = %s, first_name = %s, last_name = %s, location = %s, city = %s where user_id = %s",
                (kwargs.get("username"), kwargs.get("first_name"), kwargs.get("last_name"), kwargs.get("location"), kwargs.get("city"), kwargs.get("user_id"))
            )
            db_config.commit()
    except Exception as e:
        print(e)
        return False
    else:
        return True


