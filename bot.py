import os
import logging
import asyncio
import threading

from aiogram import Bot, Dispatcher
from aiogram.types import Update, BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from flask import Flask, request

from handlers import start, test_delivery, payment, settings

# Получаем переменные окружения
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET", "secure123")
WEBHOOK_URL = os.getenv("WEBHOOK_URL", "https://your-project-name.up.railway.app")

# Настройка бота и диспетчера
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher(storage=MemoryStorage())
dp.include_routers(start.router, test_delivery.router, payment.router, settings.router)

# Настройка Flask
app = Flask(__name__)
logging.basicConfig(level=logging.INFO)

@app.post(f"/webhook/{WEBHOOK_SECRET}")
async def webhook_handler():
    try:
        update = Update.model_validate(request.json)
        await dp.feed_update(bot, update)
        return "ok"
    except Exception as e:
        logging.error(f"Webhook error: {e}")
        return "error", 500

@app.get("/")
def home():
    return "Bot is alive!"

async def on_startup():
    await bot.set_webhook(f"{WEBHOOK_URL}/webhook/{WEBHOOK_SECRET}")
    await bot.set_my_commands([
        BotCommand(command="start", description="Перезапустить бота")
    ])

if __name__ == "__main__":п
    async def startup():
        await on_startup()
        await dp.start_polling(bot)

    threading.Thread(target=lambda: asyncio.run(startup())).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
