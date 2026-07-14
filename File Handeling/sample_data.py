# Create a sample text file with 10 lines, read and print 3rd and 4th lines from file.
with open("sample_data.txt", "w") as file:
    file.write("Line 1: Python is powerful.\n")
    file.write("Line 2: File handling is fun.\n")
    file.write("Line 3: Practice makes perfect.\n")
    file.write("Line 4: Always indent properly.\n")
    file.write("Line 5: Errors teach valuable lessons.\n")
    file.write("Line 6: Keep learning new things.\n")
    file.write("Line 7: Debugging sharpens your logic.\n")
    file.write("Line 8: Simplicity is the key.\n")
    file.write("Line 9: Code with consistency.\n")
    file.write("Line 10: Finish strong!\n")

print("sample_data.txt file created successfully.")

with open("sample_data.txt", "r") as file:
    lines = file.readlines()  

print("The 3rd line is:", lines[2].strip())
print("The 5th line is:", lines[4].strip())
