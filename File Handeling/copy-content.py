#Program to copy contents from one file to another file.
with open("sourcefile.txt", "r") as file:
      content = file.read()

with open("copyfile.txt", "w") as file:
      
   file.write(content)

