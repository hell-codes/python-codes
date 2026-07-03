#Create a dictionary with integers as keys and their squares as values
n = int(input("Enter the number of integers: "))

squares_dict = {}

for i in range(1, n + 1):
    squares_dict[i] = i ** 2 

print("Dictionary of squares:", squares_dict)
