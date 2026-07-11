# Program to read file and count frequency of each word using a dictionary
with open("sample.txt", "r") as file:
    count_dict = {}
    for line in file:
        words = line.split() 
        for word in words:
            if word in count_dict:
                count_dict[word] += 1  
            else:
                count_dict[word] = 1   

for word, count in count_dict.items():
    print(f"{word}: {count}")
