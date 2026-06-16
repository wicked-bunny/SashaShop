from aiogram import Router, types, F
import logging
from Bot.SashaShop.Interfaces import IProductRepository

router = Router()


@router.message(F.text == "Профіль")
async def catalog(message: types.Message, repository: IProductRepository):
    tabs = await repository.get_all_main_tabs()
    if  not tabs:
        logging.error("Tabs not found")
        await message.answer("Вибачте, наразі цей ресурс недоступний.")
        return #
    profile_data = None
    for tab in tabs:
        if isinstance(tab, dict) and tab.get('Tab name') == 'Profil':
            profile_data = tab['Text']
            break


    # Якщо знайшли дані для профілю — відправляємо, інакше — повідомляємо про помилку
    if profile_data:
        await message.answer(text=str(profile_data))
    else:
        logging.warning(f"У отриманих вкладках немає ключа 'Profil'. Структура: {tabs}")
        await message.answer("Цієї кнопки у даному ресурсі не існує або вона налаштована некоректно.")