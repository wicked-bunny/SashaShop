from aiogram import Bot
from aiogram.types import BotCommand
from lexicon import LexiconEN


async def set_start_button(bot:Bot):
     main_menu_commands = [
         BotCommand(
             command='/start',
             description=LexiconEN.set_main_menu_button()
         )
     ]
     await bot.set_my_commands(main_menu_commands)