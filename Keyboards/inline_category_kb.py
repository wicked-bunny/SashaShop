from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from callbacks import CategoriesCallback

def main_category_kb()-> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="👔Clothing", callback_data=CategoriesCallback(target="clothing").pack()), InlineKeyboardButton(text="📱Electronics", callback_data=CategoriesCallback(target="electronics").pack())],
            [InlineKeyboardButton(text="👟Shoes",callback_data=CategoriesCallback(target="shoes").pack()), InlineKeyboardButton(text="💄Beauty",callback_data=CategoriesCallback(target="beauty").pack())],
            [InlineKeyboardButton(text="🎧Accessories",callback_data=CategoriesCallback(target="accessories").pack()), InlineKeyboardButton(text="🏠Home & Living",callback_data=CategoriesCallback(target="home_living").pack())]
        ],
    )
