from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Profile"),KeyboardButton(text="Information")],
            [KeyboardButton(text="Catalog")]
        ],
    resize_keyboard=True
    )
