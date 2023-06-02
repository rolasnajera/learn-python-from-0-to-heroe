# Create a program that allows the user calculate the BMI
# The user will enter the height and the weight
# As a result the program will print the BMI calculated with the SI (system of units)
# See the link as a reference: https://www.calculator.net/bmi-calculator.html 
# Formula mass (kg) divided in height sqaure

mass = input("what is your weight?:   ")
height = input("What is you height? (in meters):   ")
result = round(float(mass) / (float(height) ** 2), 2)
print(f"your BMI calculated is: {result}")

