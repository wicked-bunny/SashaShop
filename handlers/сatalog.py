from aiogram import Router, types, F, Bot
from Interfaces import IProductRepository
from Keyboards import catalog_kb
from callbacks import BuyProductCallback


router = Router()


@router.callback_query(F.data == "catalog")
@router.message(F.text == "Catalog")
async def catalog(event: types.Message | types.CallbackQuery, repository: IProductRepository, bot: Bot):
    # Determine the ID of the chat where the photo should be sent
    if isinstance(event, types.Message):
        chat_id = event.chat.id
    else:
        await event.answer()  # Press the "Back" button to turn off the clock
        chat_id = event.message.chat.id

    # Fixed indentation and added `await` for an asynchronous request to Google Sheets
    products = await repository.get_all_products()

    if not products:
        await bot.send_message(chat_id=chat_id, text="The catalog is currently empty.")
        return

    for item in products:
        text = (
            f"🛍 <b>{item['name']}</b>\n\n"
            f"💰 Price: {item['price']} €\n"
            f"📝 Description: {item['description']}"
        )

        buy_callback = BuyProductCallback(action="buy", product_id=item["id"])

        await bot.send_photo(
            chat_id=chat_id,
            photo=item["photo"],
            caption=text,
            parse_mode="HTML",
            reply_markup=catalog_kb.generate_catalog_kb(buy_callback))

