#Count word frequency in a paragraph ignoring punctuation and case.
import string
paragraph = input("Enter a paragraph: ")
paragraph = paragraph.lower()

for char in string.punctuation:
    paragraph = paragraph.replace(char, "")

words = paragraph.split()

word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("Word Frequency:", word_freq)
