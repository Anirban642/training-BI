# Even
def is_even(number):
    return "Yes" if number % 2 == 0 else "No"

# Odd
def is_odd(number):
    return "Yes" if number % 2!= 0 else "No"

# Prime
def is_prime(number):
    if number <= 1:
        return "No"
    for i in range(2, number):
        if number % i == 0:
            return "No"
    return "Yes"    

# Factors
def get_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

# prime Factors
def get_prime_factors(number):
    prime_factors = []
    factors = get_factors(number)
    for factor in factors:
        if is_prime(factor) == "Yes":
            prime_factors.append(factor)
    return prime_factors

# input
try:
    number = int(input("Enter a number: "))
    print(f"Even: {is_even(number)}")  
    print(f"Odd: {is_odd(number)}")
    print(f"Prime: {is_prime(number)}")
    print(f"Factors: {get_factors(number)}") 
    print(f"Prime Factors: {get_prime_factors(number)}")    
except ValueError:
    print("Invalid Input.")      
            
            

# using class
class NumberAnalyzer:

    def __init__(self, number):
        self.number = number

    def is_even(self):
        return "Yes" if self.number % 2 == 0 else "No"

    def is_odd(self):
        return "Yes" if self.number % 2 != 0 else "No"

    def is_prime(self):
        if self.number <= 1:
            return "No"

        for i in range(2, self.number):
            if self.number % i == 0:
                return "No"

        return "Yes"

    def get_factors(self):
        factors = []

        for i in range(1, self.number + 1):
            if self.number % i == 0:
                factors.append(i)

        return factors

    def get_prime_factors(self):
        prime_factors = []

        factors = self.get_factors()

        for factor in factors:
            if factor > 1 and self.is_prime_number(factor):
                prime_factors.append(factor)

        return prime_factors

    def is_prime_number(self, number):
        if number <= 1:
            return False

        for i in range(2, number):
            if number % i == 0:
                return False

        return True


try:
    number = int(input("Enter a number: "))

    if number <= 0:
        print("Please enter a positive number")
    else:
        analyzer = NumberAnalyzer(number)

        print(f"Even: {analyzer.is_even()}")
        print(f"Odd: {analyzer.is_odd()}")
        print(f"Prime: {analyzer.is_prime()}")
        print(f"Factors: {analyzer.get_factors()}")
        print(f"Prime Factors: {analyzer.get_prime_factors()}")

except ValueError:
    print("Invalid Input.")            