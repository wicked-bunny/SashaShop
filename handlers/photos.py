# Додайте цей імпорт вгору файлу, якщо його немає

from aiogram import Router, types, F
from Bot.SashaShop.Interfaces import  IProductRepository  # Залежимо ВІД ІНТЕРФЕЙСУ

router = Router()
# Тимчасовий хендлер: ловить будь-яке фото, яке ви надсилаєте боту
@router.message(F.photo)
async def get_photo_file_id(message: types.Message):
    # message.photo[-1] — це завжди фото найбільшого (найкращої) якості
    photo_id = message.photo[-1].file_id

    # Виводимо в консоль PyCharm жирним текстом
    print("\n" + "="*50)
    print(f"ОСЬ ВАШ FILE ID ДЛЯ ТАБЛИЦІ:\n{photo_id}")
    print("="*50 + "\n")

    # Також бот продублює цей ID вам у чат, щоб було зручно скопіювати навіть з телефона
    await message.answer(f"<code>{photo_id}</code>", parse_mode="HTML")
