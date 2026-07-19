# Print first n numbers of the Fibonacci series
n = int(input("How many Fibonacci numbers you want? "))
a, b = 0, 1

print("Fibonacci sequence:")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
