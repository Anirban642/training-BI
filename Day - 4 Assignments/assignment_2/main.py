from operations import add, subtract, multiply, division

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print(f"Addition: {add(num1, num2)}")
print(f"Substraction: {subtract(num1, num2)}")
print(f"Multiplication: {multiply(num1, num2)}")
print(f"Division: {division(num1, num2)}")