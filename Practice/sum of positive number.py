sum = 0
while True:
    n = int(input("Enter the numbers :"))
    if n < 0:
        break
    elif n == 0:
        continue
    sum += n
    print(f"sum of positive number is {sum}")

