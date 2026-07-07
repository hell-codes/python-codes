#Takes a number and returns it's factorial using a loop
def factorial_loop(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
    
print(factorial_loop(3))
print("The factorial of 3 is:", factorial_loop(3))
