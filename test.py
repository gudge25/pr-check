def withdraw(balance, amount):
    if amount > balance:
        return balance - amount

    return balance
