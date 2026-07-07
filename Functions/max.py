#Takes two numbers and returns the largest number
def find_max(a, b):
    if a > b:
        return a
    else:
        return b
    
print(find_max(10,20))
print("The largest number is:", find_max(10,20))
