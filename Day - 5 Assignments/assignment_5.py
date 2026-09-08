class ForceUppercaseMeta(type):
    def __new__(cls, name, bases, dct):
        uppercase_dct = {}
        for key, value in dct.items():
            if key.startswith("__"): # avoid dunder methods
                uppercase_dct[key] = value
            else:
                uppercase_dct[key.upper()] = value

        return super().__new__(cls, name, bases, uppercase_dct)

class User(metaclass=ForceUppercaseMeta):
    name = "Anirban"
    age = 22

print(User.NAME)  # Anirban
print(User.AGE)   # 22 