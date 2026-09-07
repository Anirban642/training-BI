from calculations import Employee
from validators import SalaryValidator

employee = Employee("Anirban", 10000, 1)

validator = SalaryValidator()

try:
    validator.validate_salary(employee.basic_salary)
    validator.validate_experience(employee.experience)
    print(f"Name: {employee.name}")
    print(f"Basic Salary: {employee.calculate_basic_salary()}")
    print(f"HRA: {employee.calculate_hra()}")
    print(f"DA: {employee.calculate_da()}")
    print(f"Bonus: {employee.calculate_bonus()}")
    print(f"Tax: {employee.calculate_tax()}")
    print(f"Net Salary: {employee.calculate_net_salary()}")

except ValueError as e:
    print(e)