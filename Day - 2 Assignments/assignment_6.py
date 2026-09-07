# Sum all numbers in a nested list

nums = [10, 20, "Test", None, 3.2, [10, [40, [60, [90]]]]]

def sum_numbers(d):
    total = 0
    for i in d:
        if isinstance(i, list):
            total += sum_numbers(i)
        elif isinstance(i, (int, float)):
            total += i
    return total

result = sum_numbers(nums)

print(f"Sum: {result}")