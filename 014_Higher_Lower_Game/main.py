from game_data import data
from art import logo, vs
import os
import random

print("welcome to the")
print(logo)
print("Let's the games begin!\n")


GAME_START = bool
COMPARE_ONE = []
COMPARE_TWO = []
SCORE = int()
GUESS = int()

def play_game(GAME_START):
    GAME_START = True
    
def randomize():
    return random.choice(data)

def verification(one, two):
    if one['follower_count'] > two['follower_count']:
        return 1
    else:
        return 2

def randomize():
    COMPARE_ONE = randomize()
    COMPARE_TWO = randomize()
    name_one = COMPARE_ONE['name']
    name_two = COMPARE_TWO['name']
    return "Your score: {SCORE}\n {name_one} \n {vs} \n {name_two}"

answer = input("Would you like to play?\nYes(y) or No(n):")

while answer == 'y':

    randomize()

    while GUESS not in [1,2]:
        GUESS = int(input("Who has more followers?:\nThe first (1) or the second one (2)?:"))
        if GUESS not in [1,2]:
            print("Your answer is not in the options.\nPlease type it again!")
        
        right_option = verification(COMPARE_ONE,COMPARE_TWO)
        if GUESS == right_option:
            SCORE += 1
            print("YOU GOT IT RIGHT!")
            print(f"{COMPARE_ONE['name']} has {COMPARE_ONE}[follower_count].\n{COMPARE_TWO['name']} has {COMPARE_TWO['follower_count']}")
        else:
            print("AHHH\nYou Lose...\That is not the right answer.")
            print(f"{COMPARE_ONE['name']} has {COMPARE_ONE}[follower_count].\n{COMPARE_TWO['name']} has {COMPARE_TWO['follower_count']}")
            print("Game Over")
            print(SCORE)

    
