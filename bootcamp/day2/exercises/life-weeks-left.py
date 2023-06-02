# Write a program that allows the user the years left in their life,
# the months and the days.
# Based on an average age of 90 years.
# The user will enter their current year.
# The program will print the years, months and days left.

current_years = input("What is your current age (in years):\n")
years_left = 90 - int(current_years)
months = years_left * 12
weeks = years_left * 52
days = years_left * 365
print(f"You still have {years_left} years, {months} months, {weeks} weeks, {days} days left.")

