# Input numbers and print maximum and minimum values in the list
numbers = input("Enter numbers: ")
num_list = [int(num) for num in numbers.split()]

maximum = max(num_list)
minimum = min(num_list)
print("List:",num_list)

print("Maximum value:", maximum)
print("Minimum value:", minimum)
