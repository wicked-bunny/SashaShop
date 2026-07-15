from aiogram import Router, types, F, Bot
from repositories.unit_of_work import IUnitOfWork
from Keyboards import catalog_kb
from callbacks import BuyProductCallback, MainTabsCallback
from lexicon import ErrorEN, LexiconEN

router = Router()



@router.message(F.text == "orders")
@router.callback_query(MainTabsCallback.filter(F.target == "orders"))
async def orders(event: types.Message | types.CallbackQuery):
        #TODO: imlemenet logik
        await event.answer(text=ErrorEN.currently_unavailable())
