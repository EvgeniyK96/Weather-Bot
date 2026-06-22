import os
from dotenv import load_dotenv

load_dotenv()


bot_token = os.getenv("BOT_TOKEN", "")
weather_api_key = os.getenv("API_KEY", "0")

DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://", 1)
    elif DATABASE_URL.startswith("postgresql://") and "+asyncpg" not in DATABASE_URL:
        DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)

TIMEZONE = os.getenv("TIMEZONE", "Asia/Almaty")