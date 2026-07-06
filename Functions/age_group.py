#Takes person's age and prints the age group
def age_group(age):
    if age < 13:
        return 'Child'
    elif age >= 13 and age <=19:
        return 'Teenager'
    else:
        return 'Adult'
    
print(age_group(18))
print("You are a:", age_group(18))
