# Checks if password is strong based on given criteria
def is_strong_password(p):
    if len(p) < 8: 
        return False
    has_upper = any(c.isupper() for c in p)  
    has_lower = any(c.islower() for c in p)  
    has_digit = any(c.isdigit() for c in p)  
    has_special = any(c in "@#$%^&*!" for c in p)  
    return has_upper and has_lower and has_digit and has_special

print(is_strong_password("Password1!"))  
print(is_strong_password("weakpass"))    
