class InvalidPinError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class ATM:
    def __init__(self):
        self.pin = "1234"
        self.balance = 5000

    def validate_pin(self, pin):
        if len(pin) != 4 or not pin.isdigit():
            raise InvalidPinError("PIN must be exactly 4 digits")
        if pin != self.pin:
            raise InvalidPinError("Incorrect PIN")

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientBalanceError("Not enough balance")
        self.balance -= amount

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be positive")
        self.balance += amount

    def change_pin(self, old_pin, new_pin):
        if old_pin != self.pin:
            raise InvalidPinError("Incorrect old PIN")
        if len(new_pin) != 4 or not new_pin.isdigit():
            raise InvalidPinError("PIN must be exactly 4 digits")
        self.pin = new_pin

atm = ATM()

attempts = 0
while attempts < 3:
    pin = input("Enter PIN: ")
    try:
        atm.validate_pin(pin)
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
        print(f"Balance: {atm.check_balance()}")

    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: "))
            atm.withdraw(amount)
            print("Withdrawal successful")
            print(f"Balance: {atm.check_balance()}")
        except InvalidAmountError as e:
            print(e)
        except InsufficientBalanceError as e:
            print(e)
        except ValueError:
            print("Invalid amount")

    elif choice == "3":
        try:
            amount = float(input("Enter deposit amount: "))
            atm.deposit(amount)
            print("Deposit successful")
            print(f"Balance: {atm.check_balance()}")
        except InvalidAmountError as e:
            print(e)
        except ValueError:
            print("Invalid amount")

    elif choice == "4":
        try:
            old_pin = input("Enter old PIN: ")
            new_pin = input("Enter new PIN: ")
            atm.change_pin(old_pin, new_pin)
            print("PIN changed successfully")
        except InvalidPinError as e:
            print(e)

    elif choice == "5":
        print("Thank you for using the ATM")
        break

    else:
        print("Invalid choice")