class AccountNotFoundError(Exception):
    pass

class NegativeAmountError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

class DuplicateAccountError(Exception):
    pass

def create_account(accounts, account_number, name, balance):
    if account_number in accounts:
        raise DuplicateAccountError("No duplicates allowed")
    if balance < 0:
        raise NegativeAmountError("Balance must be +ve")
    account = {
        "account_number": account_number,
        "name": name,
        "balance": balance
    }
    accounts[account_number] = account

def deposit(accounts, account_number, amount):
    if account_number not in accounts:
        raise AccountNotFoundError("A/c not found")
    if amount < 0:
        raise NegativeAmountError("Amount must be +ve")
    accounts[account_number]["balance"] += amount

def withdraw(accounts, account_number, amount):
    if account_number not in accounts:
        raise AccountNotFoundError("A/c not found")
    if amount < 0:
        raise NegativeAmountError("Amount must be +ve")
    if amount > accounts[account_number]["balance"]:
        raise InsufficientBalanceError("Not enough balance")
    accounts[account_number]["balance"] -= amount

def transfer(accounts, from_account, to_account, amount):
    if from_account not in accounts:
        raise AccountNotFoundError("A/c not found")
    if to_account not in accounts:
        raise AccountNotFoundError("A/c not found")
    if amount < 0:
        raise NegativeAmountError("Amount must be +ve")
    if amount > accounts[from_account]["balance"]:
        raise InsufficientBalanceError("Not enough balance")
    accounts[from_account]["balance"] -= amount
    accounts[to_account]["balance"] += amount

def get_balance(accounts, account_number):
    if account_number not in accounts:
        raise AccountNotFoundError("A/c not found")
    return accounts[account_number]["balance"]

accounts = {
    "ACC1001": {
        "account_number": "ACC1001",
        "name": "Poku",
        "balance": 5000
    }
}

while True:
    print("\n1. Create account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check balance")
    print("5. Transfer")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            account_number = input("Enter account number: ")
            name = input("Enter name: ")
            balance = float(input("Enter initial balance: "))
            create_account(accounts, account_number, name, balance)
            print("Account created successfully")
        except DuplicateAccountError as e:
            print(e)
        except NegativeAmountError as e:
            print(e)
        except ValueError:
            print("Invalid amount")

    elif choice == "2":
        try:
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            deposit(accounts, account_number, amount)
            print("Amount deposited successfully")
        except AccountNotFoundError as e:
            print(e)
        except NegativeAmountError as e:
            print(e)
        except ValueError:
            print("Invalid amount")

    elif choice == "3":
        try:
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            withdraw(accounts, account_number, amount)
            print("Amount withdrawn successfully")
        except AccountNotFoundError as e:
            print(e)
        except NegativeAmountError as e:
            print(e)
        except InsufficientBalanceError as e:
            print(e)
        except ValueError:
            print("Invalid amount")

    elif choice == "4":
        try:
            account_number = input("Enter account number: ")
            balance = get_balance(accounts, account_number)
            print(f"Balance: {balance}")
        except AccountNotFoundError as e:
            print(e)

    elif choice == "5":
        try:
            from_account = input("Enter sender account: ")
            to_account = input("Enter receiver account: ")
            amount = float(input("Enter transfer amount: "))
            transfer(accounts, from_account, to_account, amount)
            print("Amount transferred successfully")
        except AccountNotFoundError as e:
            print(e)
        except NegativeAmountError as e:
            print(e)
        except InsufficientBalanceError as e:
            print(e)
        except ValueError:
            print("Invalid amount")

    elif choice == "6":
        print("Thank you for using the banking system")
        break

    else:
        print("Invalid choice")