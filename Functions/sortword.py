#Returns the list of words sorted by length (ascending)
def sort_words_by_length(words):
    return sorted(words, key=len)

words = "apple", "cat", "banana", "dog"
print(sort_words_by_length(words))  
