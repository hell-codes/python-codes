sum = 0
while True:
    a = int(input("Enter any number:"))
    if a == 0:
        break
    elif a < 0:
        continue
    sum += a
    print(sum)