from aiogram import Router,F,types

import lexicon
from callbacks import MainTabsCallback
from repositories.unit_of_work import IUnitOfWork
import logging

router = Router()

@router.message(F.text == "Information")
@router.callback_query(MainTabsCallback.filter(F.target == "bot_info"))
async def info(event: types.Message | types.CallbackQuery):
    if isinstance(event, types.CallbackQuery):
        # 1. Обов'язково відповідаємо на кнопку, щоб вона не "зависала"
        await event.answer()
        # 2. Редагуємо текст у поточному меню на інформаційний
        await event.message.edit_text(text=lexicon.LexiconEN.info_text(), parse_mode="HTML")
    else:
        # Якщо це текстове повідомлення — просто відправляємо нову відповідь
        await event.answer(text=lexicon.LexiconEN.info_text(), parse_mode="HTML")