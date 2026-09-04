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
            