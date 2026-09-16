from calculations import calculate_basic_salary, calculate_hra, calculate_da, calculate_bonus, calculate_tax, calculate_net_salary
from validators import validate_salary, validate_experience

employee = {
    "name": "Anirban",
    "basic_salary": 10000,
    "experience": 1
}

try:
    validate_salary(employee["basic_salary"])
    validate_experience(employee["experience"])

    print(f"Name: {employee['name']}")
    print(f"Basic Salary: {calculate_basic_salary(employee)}")
    print(f"HRA: {calculate_hra(employee)}")
    print(f"DA: {calculate_da(employee)}")
    print(f"Bonus: {calculate_bonus(employee)}")
    print(f"Tax: {calculate_tax(employee)}")
    print(f"Net Salary: {calculate_net_salary(employee)}")

except ValueError as e:
    print(e)