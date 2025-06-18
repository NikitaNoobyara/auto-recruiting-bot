
from aiogram import Router, types, F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import CallbackQuery
from services.db import get_user, set_test_used
from services.telethon_sender import send_single_test_message

router = Router()

@router.callback_query(F.data == "test")
async def handle_test(callback: CallbackQuery):
    user = get_user(callback.from_user.id)
    if not user:
        await callback.message.answer("❌ Ошибка: пользователь не найден.")
        return

    if user["test_used"]:
        await callback.message.answer("⚠️ Вы уже использовали тестовую рассылку.")
        return

    if not user["groups"] or not user["templates"]:
        await callback.message.answer("⚠️ Сначала добавьте группы и шаблоны в настройках.")
        return

    group = user["groups"][0]
    template = user["templates"][0]

    result = await send_single_test_message(callback.from_user.id, group, template)
    if result:
        set_test_used(callback.from_user.id)
        await callback.message.answer("✅ Тестовое сообщение отправлено.")
    else:
        await callback.message.answer("❌ Не удалось отправить тест.")
