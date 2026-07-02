# Program to compare two lists based on length, sum, and common values

list1 = [int(x) for x in input("Enter integers for first list: ").split()]
list2 = [int(x) for x in input("Enter integers for second list: ").split()]
same_length = len(list1) == len(list2)
same_sum = sum(list1) == sum(list2)
common_values = set(list1) & set(list2)
print("Both lists have the same length:", same_length)
print("Both lists have the same sum:", same_sum)

if common_values:
       print("Common values in both lists:", list(common_values))
else:
       print("There are no common values between the lists.")
