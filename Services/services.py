import gspread
from google.oauth2.service_account import Credentials

# Налаштування доступу за допомогою вашого файлу ключів
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)
###sdfsdfsdf
def get_catalog_from_sheets():
    try:
        # Відкриваємо таблицю за її точною назвою
        sheet = client.open("Назва вашої Google Таблиці").worksheet("Products")

        # Отримуємо всі рядки у вигляді списку словників (ключі — це заголовки першого рядка)
        return sheet.get_all_records()
    except Exception as e:
        print(f"Помилка зчитування таблиці: {e}")
        return []
