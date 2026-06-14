import asyncio
import os
from pathlib import Path

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from handlers import register_routers
from Repositorys.Google_Sheets_Repository import GoogleSheetsProductRepository
import logging
import sys


logging.basicConfig(
    level=logging.INFO,  # Показуватиме всі важливі події та оновлення
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)  # Виводити лог прямо в консоль PyCharm
    ]
)

# Динамічно знаходимо файл .env на один рівень вище від main.py
ENV_PATH = Path(__file__).resolve().parent.parent.parent / "BotProjectOne_Token.env"
load_dotenv(dotenv_path=ENV_PATH)

TOKEN = os.getenv("TOKEN")

async def main():
    print("бота запущено")
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    repo = GoogleSheetsProductRepository(
        credentials_path="credentials.json",
        spreadsheet_name="Sasha Shop Table",
        worksheet_name="Products"
    )

    dp["repository"] = repo
    register_routers(dp)

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бота зупинено")
