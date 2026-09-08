class ExpenseReport:
    def __init__(self, expenses):
        self.expenses = expenses
        
    def calculate_total(self):
        total = 0
        for expense in self.expenses:
            total += expense["amount"]
        return total
    
    def group_by_category(self):
        cat_total = {}
        for expense in self.expenses:
            category = expense["category"]
            if category in cat_total:
                cat_total[category] += expense["amount"]
            else:
                cat_total[category] = expense["amount"]
        return cat_total
    
    def get_highest_category(self):
        category_total = self.group_by_category()
        high_cat = None
        high_am = 0
        for c in category_total:
            if category_total[c] > high_am:
                high_am = category_total[c]
                high_cat = c
        return high_cat
    
    def generate_report(self):
        total = self.calculate_total()
        category_total = self.group_by_category()
        highest_category = self.get_highest_category()
        print(f"Total Expense: ₹{total}")
        for category in category_total:
            print(f"{category}: ₹{category_total[category]}")
        print(f"Highest Category: {highest_category}")
    
                        
# object
expenses = [
    {"category": "Food", "amount": 500},
    {"category": "Travel", "amount": 1000},
    {"category": "Food", "amount": 300},
    {"category": "Shopping", "amount": 2000}
]

report = ExpenseReport(expenses)

report.generate_report()                