#Takes number and returns how many digits number has
def count_digits(n):
    return len(str(abs(n)))
print(count_digits(73285))
print("The number of digits in 73285 is:", count_digits(73285))
