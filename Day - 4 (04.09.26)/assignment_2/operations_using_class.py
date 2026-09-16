class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

# Creating object
calculator = Calculator()

try:
    num1 = float(input("Enter 1st number: "))
    num2 = float(input("Enter 2nd number: "))
    operation = input("Enter operation (+, -, *, /): ")
    if operation == "+":
        print(f"Result: {calculator.add(num1, num2)}")
    elif operation == "-":
        print(f"Result: {calculator.subtract(num1, num2)}")
    elif operation == "*":
        print(f"Result: {calculator.multiply(num1, num2)}")
    elif operation == "/":
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print(f"Result: {calculator.divide(num1, num2)}")
    else:
        print("Invalid operation")

except ValueError:
    print("Invalid number")