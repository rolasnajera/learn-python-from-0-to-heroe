# random word
import random

TOTAL_LIVES = 5
def get_random_word():
    words = ["mother", "children", "love", "survive", "fast", "leave", "behind"]
    return words[random.randint(0, len(words) - 1)]

def start_game():
    hidden_word = get_random_word()
    blank_spaces = ""
    for _ in range(0, len(hidden_word)):
        blank_spaces += " _ "
    print(blank_spaces)



def player_guessing(word):
    lives_left = 0
    while lives_left < TOTAL_LIVES:
        letter = input("Guess a letter:  ")
        # compare
        if is_word_complete:
            print("you won!")
            return
        lives_left += 1
    print("you loose")



def play_game():
    start_game()
    player_guessing(word)
    

continues = True
while continues:
    play_game()
    progress = input("Are your ready to play?: (Yes/no)")
    if progress == "no":
        continues = False
