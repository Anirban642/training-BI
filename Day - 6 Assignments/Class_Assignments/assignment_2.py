# list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [number * number for number in numbers]
print(squares)

even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)

# dictionary
numbers2 = [1, 2, 3, 4, 5]
squares = {number: number * number for number in numbers2}
print(squares)