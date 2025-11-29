# Simple Bank System using Functions + Dictionary

account = {"balance": 0}

def deposit(amount):
    account["balance"] += amount
    print("Amount Deposited:", amount)

def withdraw(amount):
    if amount > account["balance"]:
        print("Insufficient balance!")
    else:
        account["balance"] -= amount
        print("Amount Withdrawn:", amount)

def check_balance():
    print("Current Balance:", account["balance"])

# Testing
deposit(500)
withdraw(200)
check_balance()
