
from telethon import TelegramClient
from services.db import get_user

API_ID = 12345678  # заменить на актуальный
API_HASH = 'abc123abc123abc123abc123abc123ab'

async def send_single_test_message(user_id, group, message):
    session_name = f"user_{user_id}"
    try:
        client = TelegramClient(session_name, API_ID, API_HASH)
        await client.start()
        await client.send_message(group, message)
        await client.disconnect()
        return True
    except Exception as e:
        print(f"Ошибка при отправке: {e}")
        return False
