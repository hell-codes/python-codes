#Create number of vowels in each word of sentence and store in dictionary
sentence = input("Enter a sentence: ")
vowels = 'aeiouAEIOU'
words = sentence.split()
vowel_count_dict = {}
for word in words:
    count = sum(1 for char in word if char in vowels)
    vowel_count_dict[word] = count
    print(f"Number of vowels in '{word}': {count}")
    print("Vowel count dictionary:", vowel_count_dict)
