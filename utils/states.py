from aiogram.fsm.state import State, StatesGroup


class Registration(StatesGroup):
    name = State()
    number = State()
    age = State()
    location = State()

