# decorator
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator # initiazing it that before and after greet the words will print
def greet():
    print("Hello")

greet()

# generators
def get_numbers():
    for i in range(1, 100):
        yield i

for number in get_numbers():
    print(number)