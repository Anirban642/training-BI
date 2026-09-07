def validate_salary(salary):
    if salary <= 0:
        raise ValueError("Salary must be positive")

def validate_experience(experience):
    if experience < 0:
        raise ValueError("Experience cannot be negative")