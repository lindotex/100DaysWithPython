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

def play_game(GAME_START):
    GAME_START = True
    
def randomize():
    return random.choice(data)

answer = input("Would you like to play?\nYes(y) or No(n):")

while answer == 'y':
    COMPARE_ONE = randomize()
    COMPARE_TWO = randomize()
    print(f"{COMPARE_ONE['name']} has more than {COMPARE_ONE['follower_count']} million followers!")
    answer = input("Would you like to play?\nYes(y) or No(n):")