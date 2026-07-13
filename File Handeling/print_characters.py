#Program to read and print first 5 characters from a text file.
with open("sample.txt", "r") as file:
      content = file.read(5)
print(content)

