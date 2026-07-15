
from aiogram import Router, types, F

router = Router()
# ТTemporary handler: captures any photo you send to the bot
@router.message(F.photo)
async def get_photo_file_id(message: types.Message):
    # message.photo[-1] — це завжди фото найбільшого (найкращої) якості
    photo_id = message.photo[-1].file_id
    unic_photo_id = message.photo[-1].file_unique_id

    # Print to the PyCharm console in bold
    print("\n" + "="*50)
    print(f"ОСЬ ВАШ FILE ID ДЛЯ ТАБЛИЦІ:\n{photo_id}")
    print("="*50 + "\n")

    # The bot will also send you this ID in the chat so you can easily copy it, even from your phone
    await message.answer(f"<code>{photo_id}</code>", parse_mode="HTML")
    await message.answer(f"Unic ID:\n<code>{unic_photo_id}</code>", parse_mode="HTML")
