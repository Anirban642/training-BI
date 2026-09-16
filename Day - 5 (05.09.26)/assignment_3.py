# dunder methods
# str
class ABC:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old."
    
abc = ABC("Poku", 5)
print(abc)        
        
# __add__ method

class Number:
    def __init__(self, value):
        self.value = value
    def __add__(self, other):
        return self.value + other.value
    
num1 = Number(10)
num2 = Number(20)
print(num1 + num2)  # here actually num1 + num2 is calling num1 __add__ num2

# dataclass
from dataclasses import dataclass

@dataclass
class Random:
    name: str
    age: int
    address: str
    
random = Random("Anirban", 22, "Agarpara")
print(random)    