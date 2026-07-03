# Input students marks, calculate average and print who score above average
num_students = int(input("Enter the number of students: "))

marks_dict = {}

for i in range(1, num_students + 1):
    name = input(f"Enter name of student {i}: ")
    marks = float(input(f"Enter marks of {name}: "))
    marks_dict[name] = marks

average_marks = sum(marks_dict.values()) / num_students
print(f"\nAverage marks: {average_marks:.2f}")

print("Students who scored above average:")
for student, marks in marks_dict.items():
    if marks > average_marks:
        print(f"{student} : {marks}")
