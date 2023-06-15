# The objective is to write a program that will collect the names and bids of different people. The program should ask for each bidder's name and their bid individually.
# 
# Welcome to the secret auction program. 
# What is your name?: Angela
# 
# What's your bid?: $123
# 
# Are there any other bidders? Type 'yes' or 'no'.
# yes
# 
# If there are other bidders, the screen should clear, so you can pass your phone to the next person. If there are no more bidders, then the program should display the name of the winner and their winning bid.
# 
# The winner is Elon with a bid of $55000000000
# 
# Use your knowledge of Python dictionaries and loops to solve this challenge.

import os
print("Welcome to the secret auction program.")
players = {}
more_players = True

while more_players is True:
    name = input("What is your name?:    ")
    bid = float(input("What is your bid?:    "))
    players[name] = bid
    continue_program = input("Are there any other bidders? 'yes' or 'no' (default 'yes'):   ")
    if continue_program == "no":
        more_players = False
    os.system("clear")

highest = 0
winner = ""
for player in players:
    if players[player] > highest:
        highest = players[player]
        winner = player

print(f"The winner is {winner}")
