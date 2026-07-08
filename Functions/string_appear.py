#Takes string and counts number of times 'a' appears
def count_a(string):
    return string.lower().count('a')

print(count_a("Banana"))
print("The letter 'a' appears:", count_a("Banana"), "times")
