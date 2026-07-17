num = int(input("Enter a num:"))
if num > 1:
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            print(f"{num} is composite")
            break
    else:
        print(f"{num} is prime")
else:
    print(f"{num} is neither prime nor composite")
