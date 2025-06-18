
from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from services.db import init_user

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    init_user(message.from_user.id)

    kb = InlineKeyboardBuilder()
    kb.button(text="🧪 Тест", callback_data="test")
    kb.button(text="💳 Купить доступ", callback_data="buy")
    kb.button(text="⚙ Настроить", callback_data="settings")

    await message.answer(
        "👋 Добро пожаловать в <b>Автосистему рекрутинга</b>!\n\n"
        "Здесь ты можешь автоматизировать подбор курьеров. Начни с тестовой рассылки 👇",
        reply_markup=kb.as_markup()
    )
