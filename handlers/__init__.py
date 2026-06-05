from aiogram import Dispatcher
from Bot.SashaShop.handlers.start import router as start_router


def register_routers(dp: Dispatcher):
    dp.include_router(start_router)
