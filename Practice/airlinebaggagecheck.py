
weight = float(input("Enter baggage weight (kg): "))
travel_class = input("Enter travel class (Economy/Business): ").strip().capitalize()
if travel_class == "Business":
    free_limit = 25  # 15 + 10 extra
else:
    free_limit = 15
if weight <= free_limit:
    status = "Free"
elif free_limit < weight <= free_limit + 15:
    status = "₹500 charge"
else:
    status = "Not allowed"
print("\n------ AIRLINE BAGGAGE RESULT ------")
print(f"Travel Class  : {travel_class}")
print(f"Baggage (kg)  : {weight:.1f}")
print(f"Status        : {status}")
