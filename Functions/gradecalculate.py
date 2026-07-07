#Grade calculator based on scores
def grade_calculator(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
    
print(grade_calculator(85))
print("Your grade is:", grade_calculator(85))
