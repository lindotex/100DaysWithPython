# Hangman game Project.
# Test your knowledge in
#   - IF / ELSE
#   - Lists
#   - Strings
#   - Range()

########################################################################################################################
# Step 01:
    # 1 TODO - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
    # 2 TODO - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase!
    # 3 TODO - Check if the letter that the user guessed is one of the letters in the chosen_word. 
    
########################################################################################################################
########################################################################################################################
# Step 02:
    # 1 TODO - Create an empty list called display. For each letter in the chosen word, add "_" to display (print).
    # 2 TODO - Loop Through each position in chosen_word. If the position matches 'guess' then reveal that letter at the right position.
    # 3 TODO - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_"
    
########################################################################################################################
########################################################################################################################
# Step 03:
    # 1 TODO - Create a while loop to let user guess again
    
########################################################################################################################

import random

word_list = ["cow", "baboon", "camel"]
display= []
lives = 5
match = 0
math_word = 0

num_items = len(word_list)
random_choice = random.randint(0, num_items - 1)
chosen_word = word_list[random_choice]
match = len(chosen_word)

print(f"The chosen word is {chosen_word}")
for character in chosen_word:
    display.append("_")

while (lives != 0 and match == math_word):
    guess = str(input("Guess a letter of the random word:")).lower()
    for character in chosen_word:
        if guess == character:
            display.append(character)
            math_word += 1
            print("You Got a letter!")
        else:
            lives -=1
            display.append("_")
    print(display)
    print("game over")
            
    

