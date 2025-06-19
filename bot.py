
import os
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Update, BotCommand
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from flask import Flask, request

from handlers import start, test_delivery, payment, settings

TOKEN = os.getenv("7468870837:AAEw7sbUSJH0otExiqolp6cee598y7MDxcY")
WEBHOOK_SECRET = os.getenv("WEBHOOK_SECRET")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher(storage=MemoryStorage())
dp.include_routers(start.router, test_delivery.router, payment.router, settings.router)

# Flask-приложение
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
        BotCommand(command="start", description="Перезапуск бота"),
    ])
