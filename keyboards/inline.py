from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


buttons_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Test1', callback_data='test1'),
            InlineKeyboardButton(text='Test2', callback_data='test2')
        ]
    ]
)