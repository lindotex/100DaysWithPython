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

import random

# 1 TODO :

word_list = ["cow", "baboon", "camel"]

# Counting the number of items in the list:
num_items = len(word_list)

# Defining the random word:
random_choice = random.randint(0, num_items - 1)
    # You could replace this step with: chosen_word = random.choice(word_list)
chosen_word = word_list[random_choice]
print(f"The chosen word is {chosen_word}")

# 2 TODO:

# Getting the user's input:
guess = str(input("Guess a letter of the random word:")).lower()

# 3 TODO:

for character in chosen_word:
    if guess == character:
        print("Match")
    else:
        print("Wrong")

########################################################################################################################
# Step 02:
    # 1 TODO - Create an empty list called display. For each letter in the chosen word, add "_" to display (print).
    # 2 TODO - Loop Through each position in chosen_word. If the position matches 'guess' then reveal that letter at the right position.
    # 3 TODO - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_"
    
########################################################################################################################

# 1 TODO:
display= []

for character in chosen_word:
    # 2 TODO:
    if guess == character:
        display.append(character)
    else:
        display.append("_")

print(display)