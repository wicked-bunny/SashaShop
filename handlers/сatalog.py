from aiogram import Router, types, F
import lexicon
from Keyboards import inline_category_kb
from callbacks import MainTabsCallback, CategoriesCallback


router = Router()


@router.callback_query(CategoriesCallback.filter(F.target == "catalog"))
@router.message(F.text == "Catalog")
@router.callback_query(MainTabsCallback.filter(F.target == "catalog"))
async def catalog(event: types.Message | types.CallbackQuery):
    await event.message.answer(
        text=lexicon.LexiconEN.choose_category(),
        reply_markup= inline_category_kb.main_category_kb(),
        parse_mode="HTML",
    )

# # Determine the ID of the chat where the photo should be sent
    # if isinstance(event, types.Message):
    #     chat_id = event.chat.id
    # else:
    #     await event.answer()  # Press the "Back" button to turn off the clock
    #     chat_id = event.message.chat.id
    #
    # products = await unit_of_work.items.get_all()
    #
    # if not products:
    #     await bot.send_message(chat_id=chat_id, text=ErrorEN.empty_catalog())
    #     return
    #
    # for item in products:
    #     # Text under the item image
    #     text = LexiconEN.item_description_text(name=item.name, price=item.price, description=item.description)
    #
    #     #create callback for "Buy" button
    #     buy_callback = BuyProductCallback(action="buy", product_id=item.id)
    #
    #     await bot.send_photo(
    #         chat_id=chat_id,
    #         photo=item.file_id,
    #         caption=text,
    #         parse_mode="HTML",
    #         # passing callback on
    #         reply_markup=inline_catalog_kb.generate_catalog_kb(buy_callback))
