#Program to count how many times a value appears in a tuple

numbers = (2, 4, 6, 8, 4, 2, 4, 10, 4)

value = int(input("Enter the value to count: "))

count = numbers.count(value)

print(f"The value {value} appears {count} times in the tuple.")
