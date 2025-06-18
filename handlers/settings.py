
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from services.db import update_user_data

router = Router()

class SettingStates(StatesGroup):
    groups = State()
    templates = State()

@router.callback_query(F.data == "settings")
async def enter_settings(callback: types.CallbackQuery, state: FSMContext):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text="📥 Загрузить группы")],
            [types.KeyboardButton(text="📝 Загрузить шаблоны")]
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await callback.message.answer("Выберите, что хотите настроить:", reply_markup=kb)

@router.message(F.text.lower().startswith("http"))
async def save_groups(message: types.Message, state: FSMContext):
    groups = message.text.strip().split()
    update_user_data(message.from_user.id, "groups", groups)
    await message.answer("✅ Группы сохранены.", reply_markup=types.ReplyKeyboardRemove())

@router.message()
async def save_templates(message: types.Message, state: FSMContext):
    text = message.text.strip()
    if len(text) < 3:
        await message.answer("⚠️ Шаблон слишком короткий.")
        return
    update_user_data(message.from_user.id, "templates", [text])
    await message.answer("✅ Шаблон сохранён.", reply_markup=types.ReplyKeyboardRemove())
