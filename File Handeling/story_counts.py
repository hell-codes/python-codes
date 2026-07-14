#Program to read a file and count total number of words
with open("story.txt", "r") as file:
    text = file.read() 

words = text.split()

word_count = len(words)

print(f"Total number of words in the file: {word_count}")
