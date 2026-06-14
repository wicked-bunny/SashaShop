from aiogram import Dispatcher
from Bot.SashaShop.handlers.start import router as start_router
from Bot.SashaShop.handlers.сatalog import router as catalog_router
from Bot.SashaShop.handlers.profil import router as profil_router
from Bot.SashaShop.handlers.photos import router as photo_router


def register_routers(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(catalog_router)
    dp.include_router(profil_router)
    dp.include_router(photo_router)

