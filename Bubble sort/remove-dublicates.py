#Program to sort a list of integers using Bubble Sort and remove dublicates
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def remove_dublicates(arr):
    return list(set(arr))

N = int(input("Enter number of elemnts:"))
arr = []
for i in range(N):
    num = int(input(f"Enter element {i+1}:"))
    arr.append(num)

sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)
element_arr = remove_dublicates(sorted_arr)
print("Array after removing dublicates:", element_arr)
            
            