# write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the word TRUE occurs. 
# Then check for the number of times the letters in the word LOVE occurs. 
# Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."
# e.g.
name1 = "Rolas Najera"
name2 = "Jess Pureco"
# T occurs 0 times
# R occurs 2 time
# U occurs 1 times
# E occurs 2 times
# Total = 5
# L occurs 0 time
# O occurs 2 times
# V occurs 0 times
# E occurs 2 times
# Total = 4
# Love Score = 54
# Print: "Your score is 54."

## hints -> methods lower() and count()
