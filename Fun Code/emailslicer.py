email = input("Enter your email: ")
username = email.split('@')[0]
domain = email.split('@')[1]

print(f"Username: {username}")
print(f"Domain: {domain}")
