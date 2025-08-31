def display(balance):
    print(f"Your current balance is ${balance:.2f}")

def deposit(balance):
    while True:
        try:
            deposit_amount = float(input("How much would you like to deposit?: "))
            if deposit_amount > 0:
                balance += deposit_amount
                print(f"You have deposited ${deposit_amount:.2f}")
                return balance
            else:
                print("Only enter a number above 0 please")
        except ValueError:
            print("Only enter a valid amount please")

def withdraw(balance):
    while True:
        try:
            withdraw_amount = float(input("How much would you like to withdraw?: "))
            if balance >= withdraw_amount > 0:
                balance -= withdraw_amount
                print(f"You have withdrawn ${withdraw_amount:.2f}")
                return balance
            else:
                print(f"Only enter a number between 0 and your balance (${balance:.2f}) please")
        except ValueError:
            print("Only enter a valid amount please")

balance = 0

print("-----------BANKING PROGRAM-----------")

while True:
    print("\n1. Show balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit\n")
    
    try:
        option = int(input("Enter your choice (1 - 4): "))
    except ValueError:
        print("Please enter a valid choice (1-4).")
        continue

    match option:
        case 1:
            display(balance)
        case 2:
            balance = deposit(balance)
        case 3:
            balance = withdraw(balance)
        case 4:
            break
        case _:
            print("That is not an option")

print("Have a good day!")
