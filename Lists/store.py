#Program to store words whose first letter occurs again within the word
words = input("Enter words: ").split()

result = []

for word in words:
    if len(word) > 1 and word[0].lower() in word[1:].lower():
        result.append(word)

print("Words whose first letter occurs again within the word:", result)
