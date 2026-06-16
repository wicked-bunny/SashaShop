from aiogram import Router,F,types
from Bot.SashaShop.Repositorys.Google_Sheets_Repository import IProductRepository
import logging

router = Router()

@router.message(F.text == "Інформація")
async def info(message: types.Message, repository: IProductRepository):
    tabs = await repository.get_all_main_tabs()
    if  not tabs:
        logging.error("Tabs not found")
        await message.answer("Вибачте, наразі цей ресурс недоступний.")
        return #
    profile_data = None
    for tab in tabs:
        if isinstance(tab, dict) and tab.get('Tab name') == 'Info':
            profile_data = tab['Text']
            break


    # Якщо знайшли дані для профілю — відправляємо, інакше — повідомляємо про помилку
    if profile_data:
        await message.answer(text=str(profile_data))
    else:
        logging.warning(f"У отриманих вкладках немає ключа 'Profil'. Структура: {tabs}")
        await message.answer("Цієї кнопки у даному ресурсі не існує або вона налаштована некоректно.")
