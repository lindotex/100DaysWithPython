# Hangman game Project.
# Test your knowledge in
#   - IF / ELSE
#   - Lists
#   - Strings
#   - Range()
# Hangman game Project.
# Test your knowledge in
#   - IF / ELSE
#   - Lists
#   - Strings
#   - Range()

# Step 01:
    # 1 TODO - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
    # 2 TODO - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase!
    # 3 TODO - Check if the letter that the user guessed is one of the letters in the chosen_word. 

import random

# 1 TODO :

word_list = ["cow", "baboon", "camel"]

# Counting the number of items in the list:
num_items = len(word_list)

# Defining the random word:
random_choice = random.randint(0, num_items - 1)
chosen_word = word_list[random_choice]

print(chosen_word)

# 2 TODO:

# Getting the user's input:
guess = str(input("Guess a letter of the random word:")).lower()

# 3 TODO:

for character in chosen_word:
    if guess == character:
        print("Match")
    else:
        print("Missed")