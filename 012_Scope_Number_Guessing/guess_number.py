#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

print(logo)
print("welcome to Guess Game")

level = True
guess_tries = 0
guess_number = 0
random_number = random.randint(0,100)

print(random_number)

while level == True:
    level_selected = input("Type your level:\n Easy (e) or Hard (h):")
    if level_selected == 'e':
        guess_tries = 10
        level = False
    elif level_selected == "h":
        guess_tries = 5
        level = False
    else:
        level = True    
        print("this is not a valid answer,\nPlease type one of the available options")
        print("\n")

def guess_tries_reduce():
    global guess_tries
    guess_tries -= 1

def is_close_answer():
    global guess_tries
    if  guess_number == random_number and guess_tries > 0:
        return "You answered correctly!\nYOU WON!!!! CONGRATULATIONS!!!!"
        
    elif guess_number > random_number and guess_tries > 0:
        guess_tries_reduce()
        return "Sorry, you guessed a higher number, try again"
    
    elif guess_number < random_number and guess_tries > 0:
        guess_tries_reduce()
        return "Sorry, you guessed a lower number, try again"
    else:
        print("Sorry....\nYou Lose.\n")

print(f"Ok, you had selected '{level_selected}', so you will have {guess_tries} guesses, ok?")
print("You will have to guess a number between 0 and 100, and as long as your answer is closer to the actual answer, I'll tell you.\n Good Luck!")

while guess_tries > 0 and is_close_answer() != "You answered correctly!\nYOU WON!!!! CONGRATULATIONS!!!!":
    print(f"Guesses: {guess_tries}")
    guess_number = int(input("Type a guess:"))
    print(is_close_answer())

if guess_tries == 0:
    print("Sorry....\nYou Lose.\n")
    
print("Game Over")
