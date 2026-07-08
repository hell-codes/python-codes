#Takes a string and returns string in reverse order using loop
def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str
print(reverse_string("Hello World"))
print("Reversed String is:", reverse_string("Hello World"))
