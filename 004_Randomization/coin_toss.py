# Generate a random number to gess "heads or tails" 
import string
import random

random_number = random.randint(0,1)

decision = string.capitalize(input("You you like to play heads or tails? Y or N"))

if decision = "Y":
    print("Ok, let's play!")
    print("...")
    if random_number == 0:
        print("It flips as Heads!")
    else:
        print("It flips as Tails!")
else:
    print("OK, let's try next time...")