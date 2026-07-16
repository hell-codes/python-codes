#A shopkeeper wants to record daily sales in a file sales.txt. 
#Write a program to append today’s sales amount to the file.
sales_amount = input("Enter today's sales amount: ")
with open("sales.txt", "a") as file:
    file.write(sales_amount + "\n")
    print("Sales amount recorded.")
    