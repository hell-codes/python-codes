#Program to sort list of student names in alphabetical order using Insertion Sort
def insertion_sort(names):
    for i in range(1, len(names)):
        key = names[i]
        j = i - 1
        while j >= 0 and key < names[j]:
            names[j + 1] = names[j]
            j -= 1
        names[j + 1] = key
    return names

N = int(input("Enter number of students: "))
student_names = []

for i in range(N):
    name = input("Enter name of student {}: ".format(i + 1))
    student_names.append(name)

sorted_names = insertion_sort(student_names)

print("\nSorted student names in alphabetical order:")
for name in sorted_names:
    print(name)
