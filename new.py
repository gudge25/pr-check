def withdraw(balance, amount):
    if amount > balance:
        return balance

    return balance - amount
