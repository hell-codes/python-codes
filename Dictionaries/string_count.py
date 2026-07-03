#Create a dictionary from a string and count each character
string = 'w3resource'
freq = {}

for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character Frequency Dictionary:", freq)
