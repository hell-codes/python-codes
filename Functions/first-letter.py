#Takes a word and prints the first letter
def first_letter(word):
    if len(word) == 0:
        return ''
    return word[0]
print(first_letter("Welcome"))
print("The first letter is:", first_letter("Welcome"))
