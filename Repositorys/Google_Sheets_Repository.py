# Файл: google_sheets_repository.py
import gspread
from google.oauth2.service_account import Credentials
from typing import List, Dict, Any
from Bot.SashaShop.Interfaces import IProductRepository

class GoogleSheetsProductRepository(IProductRepository):
    def __init__(self, credentials_path: str, spreadsheet_name: str, worksheet_name: str):
        scopes = [            "https://spreadsheets.google.com/feeds",
                              "https://www.googleapis.com/auth/drive"
                              ]
        creds = Credentials.from_service_account_file(credentials_path, scopes=scopes)
        self.client = gspread.authorize(creds)
        self.spreadsheet_name = spreadsheet_name
        self.worksheet_name = worksheet_name

    def get_all_products(self) -> List[Dict[str, Any]]:
        try:
            sheet = self.client.open(self.spreadsheet_name).worksheet(self.worksheet_name)
            return sheet.get_all_records()
        except Exception as e:
            print(f"Помилка Google Sheets: {e}")
            return []
