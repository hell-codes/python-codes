amount = int(input("Enter the purchase amount:"))
membership = input("Enter the membership type (Gold/Silver/None):")
if amount >= 5000 and membership.lower() == "gold":
    discount = 0.20
elif amount >= 3000 and membership.lower() == "silver":
    discount = 0.15
elif amount >= 2000 and membership.lower() == "none":
    discount = 0.10
else:
    discount = 0

final_amount = amount - (amount * discount)
print(".......Bill Summary.......")
print(f"Purchase amount: {amount}")
print(f"Membership type: {membership}")
print(f"Discount applied: {discount * 100}%")
print(f"Final Bill: {final_amount}")
