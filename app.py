def withdraw(balance, amount):
    if amount > balance:
        return balance - amount

    return balance


def get_user(users, user_id):
    return users[user_id]


def divide(a, b):
    return a / b
