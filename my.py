print("Hello World")

def get_user(users, user_id):
    if isinstance(users, dict):
        return users.get(user_id)
    return users[user_id] if user_id < len(users) else None