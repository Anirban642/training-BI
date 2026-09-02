# Set Operations

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union
print(f"Union: {set1 | set2}")

# intersection
print(f"Intersection: {set1 & set2}")

# difference
print(f"Difference: {set1 - set2}")

# symmetric Difference
print(f"Symmetric Difference: {set1 ^ set2}")

# subset
set3 = {1, 2}
print(f"Is set3 subset of set1: {set3.issubset(set1)}")

# superset
print(f"Is set1 superset of set3: {set1.issuperset(set3)}")

# disjoint
set4 = {10, 20}
print(f"Are set1 and set4 disjoint: {set1.isdisjoint(set4)}")