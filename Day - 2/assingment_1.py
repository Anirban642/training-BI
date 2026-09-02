# Collection Methods Examples
nums = [1, 2, 3, 4, 5]

# append
nums.append([6,7])
print(f"After append : {nums}")

# extend
nums.extend([9,10])
print(f"After extend: {nums}")

# insert
nums.insert(6, 8)
print(f"After insert: {nums}")

# remove
nums.remove(10)
print(f"After remove: {nums}")

# pop
nums.pop(-1) # removes the last element 
print(f"After pop: {nums}")

# clear
# nums.clear()
# print(f"After clear: {nums}") # prints empty list

# copy
nums2 = nums.copy()
print(f"After copy: {nums2}")

# count
nums2.append(2)
count = nums2.count(2)
print(f"Count of 2: {count}")

# index
idx = nums2.index(4) #  returns first occurence of 4
print(f"First 4 found in index: {idx}")

# sort
nums2.append(4)
nums.append(1)
nums2.remove([6,7]) # have to remove so that we can sort
nums2.sort()
print(f"Sorted list: {nums2}")

# reverse
nums2.reverse()
print(f"Reversed List: {nums2}")

# Tuple Methods Examples

months = ("January", "February", "March", "April", "May")

# access
print(f"First month: {months[0]}")

# count
months2 = ("January", "February", "March", "March", "May")
count = months2.count("March")
print(f"Count of March: {count}")

# index
idx = months.index("April")
print(f"Index of April: {idx}")

# length
length = len(months)
print(f"Length of tuple: {length}")

# unpacking
attributes = ("Random", 27, "Google", "Kolkata")

name, age, company, *rest = attributes

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Company: {company}")
print(f"Rest: {rest}")

# Set Methods Examples

nums = [1, 2, 3, 4, 1, 5, 6]

# set
nums_set = set(nums)
print(f"After converting list to set: {nums_set}")

# add
nums_set.add(7)
print(f"After add: {nums_set}")

# update
nums_set.update([8, 9])
print(f"After update: {nums_set}")

# remove
nums_set.remove(9)
print(f"After remove: {nums_set}")

# discard
nums_set.discard(100)  # dont give an error if element is not present
print(f"After discard: {nums_set}")

# pop
removed = nums_set.pop()
print(f"Removed element using pop: {removed}")
print(f"After pop: {nums_set}")

# copy
nums_set2 = nums_set.copy()
print(f"Copied set: {nums_set2}")

# clear
# nums_set.clear()
# print(f"After clear: {nums_set}")  # prints empty set


# Set Operations

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union
union_set = set1.union(set2)
print(f"Union: {union_set}")

# intersection
intersection_set = set1.intersection(set2)
print(f"Intersection: {intersection_set}")

# difference
difference_set = set1.difference(set2)
print(f"Difference: {difference_set}")

# symmetric difference
symmetric_difference = set1.symmetric_difference(set2)
print(f"Symmetric Difference: {symmetric_difference}")

# subset
set3 = {1, 2}

is_subset = set3.issubset(set1)
print(f"Is set3 a subset of set1: {is_subset}")

# superset
is_superset = set1.issuperset(set3)
print(f"Is set1 a superset of set3: {is_superset}")

# disjoint
set4 = {10, 20}

is_disjoint = set1.isdisjoint(set4)
print(f"Are set1 and set4 disjoint: {is_disjoint}")


# Membership
print(f"Is 3 present in set1: {3 in set1}")
print(f"Is 10 present in set1: {10 in set1}")


# Frozenset
immutable_set = frozenset({100, 200, 300, 400})
print(f"Frozenset: {immutable_set}")

# Dictionary Methods Examples

person = {
    "name": "Anirban",
    "age": 24,
    "company": "BASSETTI India"
}

# access
print(f"Name: {person['name']}")

# get
name = person.get("name")
print(f"Name using get: {name}")

# get with default value
address = person.get("address", "NA")
print(f"Address: {address}")

# keys
keys = person.keys()
print(f"Keys: {keys}")

# values
values = person.values()
print(f"Values: {values}")

# items
items = person.items()
print(f"Items: {items}")

# add
person["city"] = "Kolkata"
print(f"After adding city: {person}")

# update
person.update({"age": 22})
print(f"After update: {person}")

# remove using pop
removed = person.pop("city")
print(f"Removed value: {removed}")
print(f"After pop: {person}")

# popitem
removed_item = person.popitem()
print(f"Removed item: {removed_item}")
print(f"After popitem: {person}")

# copy
person2 = person.copy()
print(f"Copied dictionary: {person2}")

# clear
# person.clear()
# print(f"After clear: {person}")  # prints empty dictionary
