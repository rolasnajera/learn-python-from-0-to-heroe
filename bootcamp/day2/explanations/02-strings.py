my_goal =  "Learn python"
my_new_goal = 'Be a 10x developer'
my_newest_goal = "I'll be part of Apple company"
my_deepest_goal = 'I\'ll be helping others to learn programmming'

# it makes a concatanation not a sum
print("123" + "456")

# how many characters 
print(len(my_new_goal))

### INDEX ###
# L e a r n   P y t h o n
#  0 1 2 3 4 5 6 7 8 9 10 11 12
print(my_goal[0]) # l
print(my_goal[1])
print(my_goal[2])

# ...

# Negative index
print(my_goal[-1])
print(my_goal[-2])

#### Slices ####
# Important note: the last number is not included
print(my_goal[6:8]) # py
print(my_goal[:5]) # FRom start we can ommit the number zero
print(my_goal[6:]) # From a particular index till the end
print(my_goal[1:10:2]) # The third parameter is the number of jumping characters
print(my_goal[1::2]) # Example using default and third parameter
print(my_goal[::-1]) # This expression reverse the string

### Methods ###
print(my_goal.capitalize()) #First letter capitilized
print(my_goal.count("n")) # Times existed in the string

# use . to know more methods
print(len(input("What is your name?")))

# f-String
numero = 23
print(f"algo es de {23}")

