
from aiogram import Router, types, F
from aiogram.types import CallbackQuery
from services.db import set_paid

router = Router()

@router.callback_query(F.data == "buy")
async def handle_buy(callback: CallbackQuery):
    await callback.message.answer(
        "💳 Стоимость доступа — 649 ₽\n\n"
        "Оплатите по одному из способов:\n"
        "1. ЮMoney: https://yoomoney.ru/prepaid?from=layout-portal-menu\n"
        "2. СБП по номеру: +79192760321\n\n"
        "После оплаты нажмите 'Я оплатил'.",
        reply_markup=types.InlineKeyboardMarkup(
            inline_keyboard=[
                [types.InlineKeyboardButton(text="✅ Я оплатил", callback_data="confirm_payment")]
            ]
        )
    )

@router.callback_query(F.data == "confirm_payment")
async def handle_confirm(callback: CallbackQuery):
    # Здесь можно подключить API Yoomoney для автоматической проверки
    set_paid(callback.from_user.id)
    await callback.message.answer("✅ Спасибо! Доступ разблокирован.")
