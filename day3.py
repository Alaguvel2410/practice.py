balance = 5000

def check_balance():
    print("=" * 35)
    print("Current Balance : " + str(balance))
    print("=" * 35)

def deposit(amount):
    global balance
    if amount > 0:
        balance = balance + amount
        print("=" * 35)
        print("Deposited : " + str(amount))
        print("New Balance : " + str(balance))
        print("=" * 35)
    else:
        print("Invalid amount!")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance!")
    elif amount <= 0:
        print("Invalid amount!")
    else:
        balance = balance - amount
        print("=" * 35)
        print("Withdrawn : " + str(amount))
        print("Remaining Balance : " + str(balance))
        print("=" * 35)

check_balance()
deposit(1000)
withdraw(2000)
check_balance()
