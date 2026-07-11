#Program to read file and display only the lines that contain more than 20 characters.
with open("info.txt", "r") as file:
     lines = file.readlines()
for line in lines:
    if len(line) > 20:
        print(line.strip())
    
