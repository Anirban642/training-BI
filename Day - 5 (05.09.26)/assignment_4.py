from dataclasses import dataclass, InitVar

@dataclass
class User:
    name: str
    age: int
    password: InitVar[str]

    def __post_init__(self, password):
        print(f"Password received for {self.name}")

user = User("Anirban", 22, "12345678")
print(user.name)
print(user.age)
# print(user.password) 
# throws an error that User object has no attribute named password, as 
# we initialized password as InitVar