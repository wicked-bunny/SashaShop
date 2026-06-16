from aiogram import Router,F,types

from Bot.SashaShop.handlers.сatalog import BuyProductCallback

router = Router()

@router.callback_query(BuyProductCallback.filter(F.action == "buy"))
async def process_buy_product(callback: types.CallbackQuery, callback_data: BuyProductCallback):
    await callback.answer()  # Гасимо годинник на кнопці "Купити"

    # Автоматично отримуємо ID товару у правильному типі (int)
    product_id = callback_data.product_id

    # TODO: Тут потрібно отримати товар за ID з репозиторію та надіслати реквізити/форму замовлення
    await callback.message.answer(f"Ви обрали товар з ID: {product_id}. Готуємо замовлення...")
