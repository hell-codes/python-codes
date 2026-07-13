#Program to write favourite quotes to a file and read them with line numbers
quotes = []
n = int(input("How many favourite quotes do you want to enter? "))

for i in range(n):
    quote = input(f"Enter quote {i + 1}: ")
    quotes.append(quote)

with open("quotes.txt", "w") as file:
    for quote in quotes:
        file.write(quote + "\n")

print("\nYour favourite quotes:")
with open("quotes.txt", "r") as file:
    for i, line in enumerate(file, start=1):
        print(f"{i}. {line.strip()}")
