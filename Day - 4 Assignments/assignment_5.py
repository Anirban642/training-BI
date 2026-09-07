def validate_password(password):
    errors = []
    has_upper = False
    has_lower = False
    has_number = False
    has_special = False

    # Check length
    if len(password) < 8:
        errors.append("Password must be at least 8 characters")

    # Check each character
    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_number = True
        if not char.isalnum():
            has_special = True

    # Check missing requirements
    if not has_upper:
        errors.append("Missing uppercase letter")
    if not has_lower:
        errors.append("Missing lowercase letter")
    if not has_number:
        errors.append("Missing number")
    if not has_special:
        errors.append("Missing special character")

    # Final result
    if errors:
        print("Invalid password:")
        for error in errors:
            print(f"{error}")
    else:
        print("Valid password")

password = input("Enter password: ")
validate_password(password)


# using class
class PasswordValidator:

    def __init__(self, password):
        self.password = password
        self.errors = []

    def validate_password(self):

        has_upper = False
        has_lower = False
        has_number = False
        has_special = False

        # Check length
        if len(self.password) < 8:
            self.errors.append("Password must be at least 8 characters")

        # Check each character
        for char in self.password:

            if char.isupper():
                has_upper = True

            if char.islower():
                has_lower = True

            if char.isdigit():
                has_number = True

            if not char.isalnum():
                has_special = True

        # Check missing requirements
        if not has_upper:
            self.errors.append("Missing uppercase letter")

        if not has_lower:
            self.errors.append("Missing lowercase letter")

        if not has_number:
            self.errors.append("Missing number")

        if not has_special:
            self.errors.append("Missing special character")

        # Final result
        if self.errors:
            print("Invalid password:")

            for error in self.errors:
                print(f"- {error}")

        else:
            print("Valid password")


password = input("Enter password: ")

validator = PasswordValidator(password)

validator.validate_password()