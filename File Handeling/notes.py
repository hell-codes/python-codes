# Program to write a sentence to a file and read it back
with open("notes.txt", "w") as file:
    file.write("Learning Python file handling is fun!")

with open("notes.txt", "r") as file:
    content = file.read()

print("Contents of the file:")
print(content)

