from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from callbacks import BuyProductCallback


def generate_catalog_kb(buy_callback: BuyProductCallback) -> InlineKeyboardMarkup:
    """Inline Keyboard vor Catalog Items generieren """

    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Buy 💳", callback_data=buy_callback.pack())
            ]
        ]
    )


