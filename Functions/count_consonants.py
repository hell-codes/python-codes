#takes string and count consonants 
def count_consonants(s):
    consonants = "bcdfghjklmnpqrstvwxyz"
    count = 0
    for char in s.lower():
        if char in consonants:
            count += 1
    return count

result = count_consonants("Hello, World!")
print(result)  
