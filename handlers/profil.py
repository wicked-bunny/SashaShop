from aiogram import Router, types, F
import logging
from repositories.unit_of_work import IUnitOfWork
from lexicon import ErrorEN

router = Router()


@router.message(F.text == "Profile")
async def profil(message: types.Message, unit_of_work: IUnitOfWork):
    tabs = await unit_of_work.category.get_all()

    if  not tabs:
        logging.error("Tabs not found")
        await message.answer(ErrorEN.currently_unavailable())
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