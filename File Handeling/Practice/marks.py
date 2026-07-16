#A teacher maintains student marks in marks.txt. 
#Write a program to read and display all student marks.
with open("marks.txt", "r") as file:
    marks = file.readlines()
    print("Students Marks:")
    for line in marks:
        print(line.strip())
        