class SalaryValidator:
    def validate_salary(self, salary):
        if salary <= 0:
            raise ValueError("Salary must be +ve")

    def validate_experience(self, experience):
        if experience <= 0:
            raise ValueError("Experience must be +ve")