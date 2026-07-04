# Program to keep only valid values from user list

valid_values = [int(x) for x in input("Enter valid values: ").split()]

nums = [int(x) for x in input("Enter numbers: ").split()]

result = []
for x in nums:
    if x in valid_values:
        result.append(x)

print("Valid numbers are:", result)

