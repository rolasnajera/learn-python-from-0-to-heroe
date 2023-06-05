# if condition:
#    do this
# else:
#    do this

print("This is the amazing pumpo dico!")
age = int(input("What is your age?:  "))

# Also we have here compund statement -> header -> body (here the body is running only if the condition is true)
if age < 21:
# here we have indentention to know the body of the if statement
    print("Really sorry, you can't enter to the pumpo disco")
else:
    print("Welcome to the pumpo disco!")

name = "Rolas"
if name == "Rolas":
    print("hello " + name + "!")
else:
    print("hello, your name is not Rolas!")

number = int(input("Enter a number:  "))
if number > 0:
    print("It's a positive number")
elif number == 0:
    print("It's zero")
else:
    print("It's a negative number")

# Nested if / else

if age > 20:
    if age > 65:
        print("you can enter for free")
    else:
        print("your ticket cost 25")
else:
    print("you cannot enter")

# Using logical operators
if age > 20 and age < 65:
    print("Your ticket cost $25")
elif age > 65:
    print("Your ticket si for free")
else:
    print("You cannot enter")
