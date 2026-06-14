
from aiogram import Router, types, F
from Bot.SashaShop.Interfaces import  IProductRepository  # Залежимо ВІД ІНТЕРФЕЙСУ


router = Router()

@router.message(F.text == "Каталог")
async def info(message: types.Message, repository: IProductRepository):
    # Код не знає, що це Google Sheets, він просто викликає метод інтерфейсу
    products = repository.get_all_products()

    if not products:
        await message.answer("Каталог наразі порожній.")
        return

    for item in products:
        text = (
            f"🛍 <b>{item['name']}</b>\n\n"
            f"💰 Ціна: {item['price']} грн\n"
            f"📝 Опис: {item['description']}"
        )

        await message.answer_photo(
            photo=item["photo"],  # Сюди підставиться File ID з таблиці
            caption=text,
            parse_mode="HTML"
        )
