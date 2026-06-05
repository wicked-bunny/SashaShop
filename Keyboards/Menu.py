from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Профіль")],
            [KeyboardButton(text="Каталог")]
        ],
    resize_keyboard=True
    )
