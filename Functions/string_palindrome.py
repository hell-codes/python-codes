#Takes a string and checks if it's a palindrome or not
def is_palindrome(x):
    x = x.lower().replace(" ", "")  
    return x == x[::-1]  

print(is_palindrome("Hello"))      
print(is_palindrome("Racecar"))      
print(is_palindrome("Level"))
