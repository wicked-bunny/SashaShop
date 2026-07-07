from aiogram import Router,types
from aiogram.filters import Command
from Keyboards.Menu import main_menu_kb
router = Router()


@router.message(Command("start"))
async def start_bot(message: types.Message):
    await message.answer(
        f"Hi, {message.from_user.first_name} This is the [STORE NAME] store",
            reply_markup=main_menu_kb()
    )

