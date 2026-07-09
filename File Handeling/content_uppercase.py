#Program to reada file and print its content in uppercase.
with open("sample.txt", "r") as file:
      content = file.read()
print(content.upper())

