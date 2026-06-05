import asyncio
import os
from pathlib import Path

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import register_routers

# Динамічно знаходимо файл .env на один рівень вище від main.py
ENV_PATH = Path(__file__).resolve().parent.parent.parent / "BotProjectOne_Token.env"
load_dotenv(dotenv_path=ENV_PATH)

TOKEN = os.getenv("TOKEN")

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    print("бота запущено")
    register_routers(dp)

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бота зупинено")
