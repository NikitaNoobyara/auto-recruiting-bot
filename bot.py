import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties  # 👈 вот это добавляем
import logging

from handlers import start, test_delivery, payment, settings

TOKEN = "7468870837:AAEw7sbUSJH0otExiqolp6cee598y7MDxcY"

async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode="HTML")  # 👈 исправлено
    )
    dp = Dispatcher(storage=MemoryStorage())

    dp.include_routers(
        start.router,
        test_delivery.router,
        payment.router,
        settings.router
    )

    await bot.set_my_commands([
        BotCommand(command="start", description="Перезапустить бота"),
    ])

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
