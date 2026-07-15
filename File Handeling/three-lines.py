#Program to write three lines of text into a file named info.txt
with open("info.txt", "w") as file:
      file.write("This is Python file handling.\n")
      file.write("We are writing three lines of text.\n")
      file.write("Written successfully!")
      
