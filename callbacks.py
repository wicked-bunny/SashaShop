from aiogram.filters.callback_data import CallbackData


# Фабрика для безпечної передачі ID товару в кнопку
class BuyProductCallback(CallbackData, prefix="buy_prod"):
    action: str
    product_id: int
