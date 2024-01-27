from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from data.database import check_users, register_users
from keyboards.reply import number_kb, rmp, location_kb
from keyboards.inline import buttons_inline
from utils.states import Registration

router = Router()


# нету обработки старт
@router.message(Command('start'))
async def message_start(message: Message, state: FSMContext):
    checker = check_users(message.from_user.id)

    if checker:
        await message.answer('Hello', reply_markup=buttons_inline)
    else:
        await state.set_state(Registration.name)
        await message.answer('Добро пожаловать отправьте свое имя')


@router.message(Registration.name)
async def name_handler(message: Message, state: FSMContext):
    if message.text:
        await state.update_data(name=message.text)
        await state.set_state(Registration.number)

        await message.answer('Send your number, pls use button !', reply_markup=number_kb)
    else:
        await message.answer('Please enter your name!\nExample [Albert]')


@router.message(Registration.number)
async def number_handler(message: Message, state: FSMContext):
    if message.contact.phone_number:
        await state.update_data(number=message.contact.phone_number)
        await state.set_state(Registration.age)

        await message.answer('Send your age !', reply_markup=rmp)
    else:
        await message.answer('Please use button !')


@router.message(Registration.age)
async def age_handler(message: Message, state: FSMContext):
    if message.text.isdigit():
        await state.update_data(age=message.text)
        await state.set_state(Registration.location)

        await message.answer('Send your location !', reply_markup=location_kb)


@router.message(Registration.location)
async def location_handler(message: Message, state: FSMContext):
    if message.location:
        await state.update_data(location={'x': message.location.longitude, 'y': message.location.latitude})
        data = await state.get_data()
        await state.clear()

        register_users(user_id=message.from_user.id, name=data['name'], age=data['age'], phn=data['number'],
                       location=str(data['location']))

        await message.answer('Exactly', reply_markup=rmp)
        await message.bot.send_message(302137006, text=f'<b>Имя:</b> {data['name']}\n'
                                                       f'<b>Номер</b>: {data['number']}\n'
                                                       f'<b>Возраст</b>: {data['age']}\n')

        await message.bot.send_location(chat_id=302137006,
                                        longitude=float(data['location']['x']),
                                        latitude=float(data['location']['y']))
