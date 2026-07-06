# Calculates BMI and prints weight category
def bmi_calculator(weight, height):
    bmi = weight / (height ** 2) 
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    elif bmi < 30:
        print("Overweight")
    else:
        print("Obese")

bmi_calculator(70, 1.75)
bmi_calculator(85, 1.8)
bmi_calculator(50, 1.6)
