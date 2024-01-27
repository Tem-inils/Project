from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove
)

number_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отправить Контакт', request_contact=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True

)

location_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Отправить локацию', request_location=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)


rmp = ReplyKeyboardRemove()


