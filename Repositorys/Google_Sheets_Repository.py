# Файл: google_sheets_repository.py
import gspread_asyncio
from google.oauth2.service_account import Credentials
from typing import List, Dict, Any
from enum import Enum
from Bot.SashaShop.Interfaces import IProductRepository

class WorksheetsNames(str, Enum):
    MAIN_TAB = "Main Tabs"
    PRODUCTS = "Products"

class GoogleSheetsProductRepository(IProductRepository):
    def __init__(self, credentials_path: str, spreadsheet_name: str):
        self.credentials_path = credentials_path
        self.spreadsheet_name = spreadsheet_name

        # Створюємо фабрику облікових даних для асинхронного клієнта
        def get_creds():
            scopes = [
                "https://spreadsheets.google.com/feeds",
                "https://www.googleapis.com/auth/drive"
            ]
            return Credentials.from_service_account_file(self.credentials_path, scopes=scopes)

        # Ініціалізуємо менеджер асинхронних клієнтів
        self.client_manager = gspread_asyncio.AsyncioGspreadClientManager(get_creds)

    # Метод стає асинхронним (async def)
    async def get_all_products(self) -> List[Dict[str, Any]]:
        return await self.get_all_from_sheet(WorksheetsNames.PRODUCTS)

    # Метод стає асинхронним (async def)
    async def get_all_main_tabs(self) -> List[Dict[str, Any]]:
        return await self.get_all_from_sheet(WorksheetsNames.MAIN_TAB)

    # Головний метод, який тепер використовує await
    async def get_all_from_sheet(self, worksheet: WorksheetsNames) -> List[Dict[str, Any]]:
        try:
            # 1. Отримуємо асинхронний клієнт (потрібен await)
            client = await self.client_manager.authorize()

            # 2. Відкриваємо таблицю (потрібен await)
            spreadsheet = await client.open(self.spreadsheet_name)

            # 3. Отримуємо конкретний лист (потрібен await)
            sheet = await spreadsheet.worksheet(worksheet.value)

            # 4. Читаємо всі записи (потрібен await)
            return await sheet.get_all_records()
        except Exception as e:
            print(f"Помилка Google Sheets: {e}")
            return []
