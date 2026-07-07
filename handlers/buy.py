from aiogram import Router,F,types

from handlers.сatalog import BuyProductCallback

router = Router()

@router.callback_query(BuyProductCallback.filter(F.action == "buy"))
async def process_buy_product(callback: types.CallbackQuery, callback_data: BuyProductCallback):
    await callback.answer()  # Click the "Buy" button to complete the purchase

    # We automatically retrieve the product ID in the correct type (int)
    product_id = callback_data.product_id

    # TODO: Here, you need to retrieve the item by its ID from the repository and submit the payment details/order form
    await callback.message.answer(f"Ви обрали товар з ID: {product_id}. Готуємо замовлення...")
