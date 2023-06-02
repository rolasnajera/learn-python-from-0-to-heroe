# Write a program that helps the user to split the bill in a restaurant,
# adding the tip for each person.
# The user enter the amount of the bill, and the number of people to be divided
# As a result we obtain the amount for each person, pay attention to the two decimals
# after the float point.
# Output example: Each person must pay $45.66

bill_amount = float(input("Total amount:  "))
number_person = int(input("Number of people to be divided:   "))
tip = int(input("Percentage amount of tip to be added:   "))
percentage_tip = (tip * bill_amount) / 100
total_amount = bill_amount + percentage_tip
result = total_amount / number_person
print(f"Each person mut pay: {result} ")


