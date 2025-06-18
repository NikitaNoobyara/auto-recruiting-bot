
import json
import os

USERS_PATH = 'data/users.json'

os.makedirs('data', exist_ok=True)
if not os.path.exists(USERS_PATH):
    with open(USERS_PATH, 'w', encoding='utf-8') as f:
        json.dump({}, f)

def load_users():
    with open(USERS_PATH, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_users(data):
    with open(USERS_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def init_user(user_id):
    users = load_users()
    user_id = str(user_id)
    if user_id not in users:
        users[user_id] = {
            "paid": False,
            "test_used": False,
            "groups": [],
            "templates": []
        }
        save_users(users)

def set_paid(user_id):
    users = load_users()
    users[str(user_id)]["paid"] = True
    save_users(users)

def set_test_used(user_id):
    users = load_users()
    users[str(user_id)]["test_used"] = True
    save_users(users)

def get_user(user_id):
    users = load_users()
    return users.get(str(user_id), None)

def update_user_data(user_id, key, value):
    users = load_users()
    users[str(user_id)][key] = value
    save_users(users)
