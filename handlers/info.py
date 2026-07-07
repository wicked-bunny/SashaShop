from aiogram import Router,F,types
from Repositorys.Google_Sheets_Repository import IProductRepository
import logging

router = Router()

@router.message(F.text == "Information")
async def info(message: types.Message, repository: IProductRepository):
    tabs = await repository.get_all_main_tabs()
    if  not tabs:
        logging.error("Tabs not found")
        await message.answer("We're sorry, but this resource is currently unavailable.")
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
        logging.warning(f"There is no key in the received tabs 'Profil'. Structure: {tabs}")
        await message.answer("This button does not exist on this site, or it is configured incorrectly.")
