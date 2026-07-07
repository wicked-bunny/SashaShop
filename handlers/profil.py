from aiogram import Router, types, F
import logging
from Interfaces import IProductRepository

router = Router()


@router.message(F.text == "Profile")
async def catalog(message: types.Message, repository: IProductRepository):
    tabs = await repository.get_all_main_tabs()
    if  not tabs:
        logging.error("Tabs not found")
        await message.answer("We're sorry, but this resource is currently unavailable.")
        return #
    profile_data = None
    for tab in tabs:
        if isinstance(tab, dict) and tab.get('Tab name') == 'Profil':
            profile_data = tab['Text']
            break


    # If we find the profile data, we send it; otherwise, we report an error
    if profile_data:
        await message.answer(text=str(profile_data))
    else:
        logging.warning(f"The 'Profil' key is missing from the returned tabs. Structure: {tabs}")
        await message.answer("This button does not exist on this site, or it is configured incorrectly.")