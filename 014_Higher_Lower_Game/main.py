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
answer = ''
    
def randomize():
    return random.choice(data)

def verification(one, two):
    if one['follower_count'] > two['follower_count']:
        return 1
    else:
        return 2

def game_over():
    return "Game Over."

answer = str(input("Would you like to play?\nYes(y) or No(n):"))

while answer not in ['y','n']:    
    print("Your answer is not in the options.\nPlease type it again!")
    answer = str(input("try your answer again...\nPlease choose between Yes (y) or No (n):"))
        
if answer == 'n':
    print('Ok, see you next time!\nBye Bye!!!')
    print(game_over())
    
else:
    print("You got here!")
    
    while answer == 'y':
        COMPARE_ONE = randomize()
        COMPARE_TWO = randomize()
        
        print(f"\n")
        print(f"-----------------------------")
        print(f"first: {COMPARE_ONE['name']}")
        print(vs)
        print(f"Second: {COMPARE_TWO['name']}")
        print(f"-----------------------------")
        print(f"\n")
        print(f"Your Score: {SCORE}")
        print(f"\n")
        GUESS = int(input("Who has more followers?:\nThe first (1) or the second one (2)?:"))
        
        if GUESS in [1,2]:
            right_option = verification(COMPARE_ONE,COMPARE_TWO)
            if GUESS == right_option:
                SCORE += 1
                print(f"Your Score: {SCORE}")
                print("YOU GOT IT RIGHT!")
                print(f"{COMPARE_ONE['name']} has {COMPARE_ONE['follower_count']}\n{COMPARE_TWO['name']} has {COMPARE_TWO['follower_count']}")
                answer ='y'
            else:
                print(f"Your Score: {SCORE}")
                print("AH\nYou Lose...\nThat is not the right answer.")
                print(f"{COMPARE_ONE['name']} has {COMPARE_ONE['follower_count']} followers... \n{COMPARE_TWO['name']} has {COMPARE_TWO['follower_count']}!")
                print(game_over())
                answer ='n'
                print(f"Your final score was: {SCORE} points, congratulations!")
        else:
            print("Your answer is not in the options, please select between 1 or 2.") # FIX THIS!!!!!!!
    
##### BUG: 
##### Make a Loop to fix the part of repetition