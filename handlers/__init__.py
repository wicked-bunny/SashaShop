from aiogram import Dispatcher
from Bot.SashaShop.handlers.start import router as start_router
from Bot.SashaShop.handlers.сatalog import router as catalog_router
from Bot.SashaShop.handlers.profil import router as profil_router
from Bot.SashaShop.handlers.get_photoID import router as get_photoID_router
from Bot.SashaShop.handlers.info import router as info_router
from Bot.SashaShop.handlers.buy import router as buy_router



def register_routers(dp: Dispatcher):
    dp.include_router(start_router)
    dp.include_router(catalog_router)
    dp.include_router(profil_router)
    dp.include_router(get_photoID_router)
    dp.include_router(info_router)
    dp.include_router(buy_router)

