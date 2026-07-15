#A library stores book titles in books.txt. 
#Write a program to add a new book title entered by the user.
new_book = input("Enter the new book title to add: ")
with open("books.txt", "a") as file:
    file.write(new_book + "\n")
    print(f"'{new_book}' has been added to the library.")
    