from aiogram import Router,types
from aiogram.filters import Command
from Bot.SashaShop.Keyboards.Menu import main_menu_kb
router = Router()


@router.message(Command("start"))
async def start_bot(message: types.Message):
    await message.answer(
        f"Привіт, {message.from_user.first_name} це магазин [НАЗВА МАГАЗИНУ]",
            reply_markup=main_menu_kb()
    )

