from aiogram import Router, F

from aiogram.types import CallbackQuery
from aiogram.filters.callback_data import CallbackData

from aiogram.filters import Command
from aiogram.types import Message

router = Router()


# @router.callback_query(F.data.in_("test1"))
# async def more_handler(call: CallbackQuery):
#     print(call)
#     await call.bot.send_message(call.from_user.id, 'Hello My friend')
#
