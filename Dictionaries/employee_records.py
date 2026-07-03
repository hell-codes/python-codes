#Take employee records and print top 3 highest-paid employees
num_employees = int(input("Enter number of employees: "))
employees = {}

for i in range(1, num_employees + 1):
    print(f"\nEnter details for Employee {i}:")
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Employee Name: ")
    salary = float(input("Enter Employee Salary: "))
    employees[emp_id] = {'name': name, 'salary': salary}

sorted_employees = sorted(employees.items(), key=lambda x: x[1]['salary'], reverse=True)

print("\nTop 3 Highest-Paid Employees:")
for i, (emp_id, details) in enumerate(sorted_employees[:3], start=1):
    print(f"{i}. ID: {emp_id}, Name: {details['name']}, Salary: {details['salary']}")
