# Program to sort list of numbers using Insertion Sort
# and print list after every pass to show intermediate steps
def insertion_sort(numbers):
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
        print("After inserting {}: {}".format(key, numbers))
    return numbers
N = int(input("Enter number of elements: "))
number_list = []

for i in range(N):
    num = float(input("Enter element {}: ".format(i + 1)))
    number_list.append(num)

print("\nOriginal list:", number_list)
sorted_list = insertion_sort(number_list)
print("\nFinal sorted list:", sorted_list)
