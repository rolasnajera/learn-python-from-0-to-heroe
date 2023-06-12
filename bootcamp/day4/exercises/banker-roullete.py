# You are going to write a program that will select a random name from a list of names. 
# The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
# Line 8 splits the string names_string into individual names and puts them inside a
# List called names. For this to work, you must enter all the names as names followed by
# comma then space. e.g. name, name, name
# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.
# Example Output
# Michael is going to buy the meal today!

import random

names = input("Write the names separated by commas and spaces:\n")
names_list = names.split(", ")
random_person = random.randint(0, len(names_list) - 1)
print(f"{names_list[random_person]} must pay the bill.")
