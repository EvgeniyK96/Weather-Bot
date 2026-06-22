import psycopg2
from urllib.parse import urlparse, unquote
from config import DATABASE_URL


def _build_connect_params(database_url: str):
    if not database_url:
        raise RuntimeError("DATABASE_URL is not set")
    # Remove async driver marker if present (e.g. +asyncpg)
    cleaned = database_url.replace("+asyncpg", "")
    # Normalize legacy postgres:// to postgresql:// if needed
    if cleaned.startswith("postgres://"):
        cleaned = "postgresql://" + cleaned[len("postgres://"):]
    parsed = urlparse(cleaned)
    user = unquote(parsed.username) if parsed.username else None
    password = unquote(parsed.password) if parsed.password else None
    host = parsed.hostname
    port = parsed.port
    dbname = parsed.path.lstrip("/") if parsed.path else None
    params = {
        'host': host,
        'port': port,
        'dbname': dbname,
        'user': user,
        'password': password
    }
    return {k: v for k, v in params.items() if v is not None}


try:
    CONNECT = _build_connect_params(DATABASE_URL)
    db_config = psycopg2.connect(**CONNECT)
except Exception as e:
    print("Failed to connect to database:", e)
    db_config = None

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


def init_db():
    with db_config.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                user_id BIGINT UNIQUE NOT NULL,
                username VARCHAR(255),
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                phone VARCHAR(50),
                location VARCHAR(255),
                city VARCHAR(255)
            )
        """)
    db_config.commit()