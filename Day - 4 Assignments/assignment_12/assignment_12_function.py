class InvalidPinError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

def validate_pin(pin, correct_pin):
    if len(pin) != 4 or not pin.isdigit():
        raise InvalidPinError("PIN must be exactly 4 digits")
    if pin != correct_pin:
        raise InvalidPinError("Incorrect PIN")

def check_balance(balance):
    return balance

def withdraw(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Withdrawal amount must be positive")
    if amount > balance:
        raise InsufficientBalanceError("Not enough balance")
    balance -= amount
    return balance

def deposit(balance, amount):
    if amount <= 0:
        raise InvalidAmountError("Deposit amount must be positive")
    balance += amount
    return balance

def change_pin(old_pin, new_pin, correct_pin):
    if old_pin != correct_pin:
        raise InvalidPinError("Incorrect old PIN")
    if len(new_pin) != 4 or not new_pin.isdigit():
        raise InvalidPinError("PIN must be exactly 4 digits")
    return new_pin

pin = "1234"
balance = 5000

attempts = 0
while attempts < 3:
    entered_pin = input("Enter PIN: ")
    try:
        validate_pin(entered_pin, pin)
        print("PIN verified successfully")
        break
    except InvalidPinError as e:
        attempts += 1
        print(e)
else:
    print("Maximum 3 incorrect attempts exceeded")
    exit()

while True:
    print("\n1. Check balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Change PIN")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Balance: {check_balance(balance)}")

    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: "))
            balance = withdraw(balance, amount)
            print("Withdrawal successful")
            print(f"Balance: {balance}")
        except InvalidAmountError as e:
            print(e)
        except InsufficientBalanceError as e:
            print(e)
        except ValueError:
            print("Invalid amount")

    elif choice == "3":
        try:
            amount = float(input("Enter deposit amount: "))
            balance = deposit(balance, amount)
            print("Deposit successful")
            print(f"Balance: {balance}")
        except InvalidAmountError as e:
            print(e)
        except ValueError:
            print("Invalid amount")

    elif choice == "4":
        try:
            old_pin = input("Enter old PIN: ")
            new_pin = input("Enter new PIN: ")
            pin = change_pin(old_pin, new_pin, pin)
            print("PIN changed successfully")
        except InvalidPinError as e:
            print(e)

    elif choice == "5":
        print("Thank you for using the ATM")
        break

    else:
        print("Invalid choice")