#Program to remove all elements that are common between two sets.
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

common = set1.intersection(set2)

set1 -= common
set2 -= common

print(f"Set1 after removing common elements: {set1}")
print(f"Set2 after removing common elements: {set2}")
