#Program to search for a word in a file and print line numbers where it occurs
search_word = input("Enter the word to search for: ").lower()

found = False  

with open("dictionary.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        
        if search_word in line.lower():
            print(f"'{search_word}' found on line {line_number}: {line.strip()}")
            found = True

if not found:
    print(f"'{search_word}' was not found in the file.")
