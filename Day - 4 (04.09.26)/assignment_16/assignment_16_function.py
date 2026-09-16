def calculate_total(expenses):
    if not expenses:
        raise ValueError("Expenses cannot be empty")
    total = 0
    for expense in expenses:
        if not isinstance(expense["amount"], (int, float)) or expense["amount"] < 0:
            raise ValueError("Invalid amount")
        total += expense["amount"]
    return total

def group_by_category(expenses):
    if not expenses:
        raise ValueError("Expenses cannot be empty")
    category_total = {}
    for expense in expenses:
        if not isinstance(expense["amount"], (int, float)) or expense["amount"] < 0:
            raise ValueError("Invalid amount")
        category = expense["category"]
        if category in category_total:
            category_total[category] += expense["amount"]
        else:
            category_total[category] = expense["amount"]
    return category_total

def get_highest_category(expenses):
    category_total = group_by_category(expenses)
    highest_category = None
    highest_amount = 0
    for category in category_total:
        if category_total[category] > highest_amount:
            highest_amount = category_total[category]
            highest_category = category
    return highest_category

def generate_report(expenses):
    total = calculate_total(expenses)
    category_total = group_by_category(expenses)
    highest_category = get_highest_category(expenses)
    print(f"Total Expense: ₹{total}")
    for category in category_total:
        print(f"{category}: ₹{category_total[category]}")
    print(f"Highest Category: {highest_category}")

expenses = [
    {"category": "Food", "amount": 500},
    {"category": "Travel", "amount": 1000},
    {"category": "Food", "amount": 300},
    {"category": "Shopping", "amount": 2000}
]

try:
    generate_report(expenses)
except ValueError as e:
    print(e)