from aiogram import Router, types
from aiogram.filters import Command

from Keyboards.start_kb import generate_start_kb
from database.models.user import User
from lexicon import LexiconEN
from repositories.unit_of_work import IUnitOfWork

router = Router()

@router.message(Command("start"))
async def start_bot(message: types.Message, unit_of_work: IUnitOfWork):
    user_id = message.from_user.id

    existing_user = await unit_of_work.users.get_by_id(user_id)

    if not existing_user:
        new_user = User(
            id=user_id,
            fullname=message.from_user.full_name,
            username=message.from_user.username,
            tg_id=message.from_user.id
        )
        await  unit_of_work.users.add(new_user)

    else:
        # if the customer has changed their name
        if existing_user.fullname != message.from_user.full_name or existing_user.username != message.from_user.username:
            # Update data
            update_data = {
                "fullname": message.from_user.full_name,
                "username": message.from_user.username,
            }
            await unit_of_work.users.update_by_id(user_id, update_data)

    await unit_of_work.commit()

    await message.answer(
        LexiconEN.start_message(),
        reply_markup= generate_start_kb(),
        parse_mode="HTML",
    )

