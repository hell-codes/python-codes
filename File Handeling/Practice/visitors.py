#A company logs visitors in visitors.txt. 
#Write a program to count how many visitors came today.
with open("visitors.txt", "r") as file:
    visitors = file.readlines()
    print(f"Total visitors today: {len(visitors)}")
    