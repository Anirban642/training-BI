# Creating my own version of copy.deepcopy()

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def my_deep_copy(data):
    result = []
    for item in data:
        if isinstance(item, list):
            result.append(my_deep_copy(item))
        else:
            result.append(item)
    return result

matrix2 = my_deep_copy(matrix)

print(f"Original matrix: {matrix}")
print(f"Deep copied new matrix: {matrix2}")
