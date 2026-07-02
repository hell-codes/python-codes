# Program to calculate employees' gross pay and statistics
PAY_RATE = 150
NUM_EMPLOYEES = 6
hours = []
for i in range(NUM_EMPLOYEES):
    h = float(input(f"Enter hours worked by employee {i + 1}: "))
    hours.append(h)
gross_pay = []
for h in hours:
    gross_pay.append(h * PAY_RATE)
print("\n--- Employee Gross Pay ---")
for i in range(NUM_EMPLOYEES):
    print(f"Employee {i + 1}: Rs.{gross_pay[i]:.2f}")
average_pay = sum(gross_pay) / NUM_EMPLOYEES
print(f"\nAverage Pay: Rs.{average_pay:.2f}")
max_pay = max(gross_pay)
min_pay = min(gross_pay)
max_index = gross_pay.index(max_pay)
min_index = gross_pay.index(min_pay)
print(f"\nEmployee {max_index + 1} has the maximum pay: Rs.{max_pay:.2f}")
print(f"Employee {min_index + 1} has the minimum pay: Rs.{min_pay:.2f}")
