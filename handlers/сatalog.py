from aiogram import Router, types, F, Bot
from Bot.SashaShop.Interfaces import IProductRepository
from Bot.SashaShop.Keyboards import catalog_kb
from Bot.SashaShop.callbacks import BuyProductCallback


router = Router()


@router.callback_query(F.data == "catalog")
@router.message(F.text == "Каталог")
async def catalog(event: types.Message | types.CallbackQuery, repository: IProductRepository, bot: Bot):
    # Визначаємо ID чату, куди відправляти фото
    if isinstance(event, types.Message):
        chat_id = event.chat.id
    else:
        await event.answer()  # Гасимо годинник на кнопці "Назад"
        chat_id = event.message.chat.id

    # Виправлено відступи та додано await для асинхронного запиту до Google Sheets
    products = await repository.get_all_products()

    if not products:
        await bot.send_message(chat_id=chat_id, text="Каталог наразі порожній.")
        return

    for item in products:
        text = (
            f"🛍 <b>{item['name']}</b>\n\n"
            f"💰 Ціна: {item['price']} грн\n"
            f"📝 Опис: {item['description']}"
        )

        buy_callback = BuyProductCallback(action="buy", product_id=item["id"])

        await bot.send_photo(
            chat_id=chat_id,
            photo=item["photo"],
            caption=text,
            parse_mode="HTML",
            reply_markup=catalog_kb.generate_catalog_kb(buy_callback))

