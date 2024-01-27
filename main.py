import asyncio

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode

from handlers import user_commands, more_handlers


async def main() -> None:
    bot = Bot(token='6396156210:AAHR0uDD1ZlMrfeKdPAPGebgoGLYm51GW4Q', parse_mode=ParseMode.HTML)
    dp = Dispatcher()

    dp.include_router(user_commands.router)
    dp.include_router(more_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
