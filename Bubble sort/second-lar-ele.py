#Program to read N numbers, sort them using Bubble Sort and find second largest element
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def find_second_largest(arr):
    element_arr = list(set(arr))
    element_arr.sort()
    if len(element_arr) < 2:
        return None
    else:
        return element_arr[-2]

N = int(input("Enter number of elements: "))
arr = []
for i in range(N):
    num = int(input(f"Enter element {i+1}: "))
    arr.append(num)

sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
second_largest = find_second_largest(sorted_arr)
if second_largest is None:
    print("No second largest element (all elements are same).")
else:
    print("Second largest element:", second_largest)
