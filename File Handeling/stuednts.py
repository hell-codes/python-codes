#read student names and marks from a file and output the student with the highest score.
with open("students.txt", "r") as file:
     lines = file.readlines()

highest_score = -1
top_student = ""

for line in lines:
    name, score = line.split()
    score = int(score)

    if score > highest_score:
        highest_score = score
        top_student = name

print(f"Top student: {top_student} with score {highest_score}")
