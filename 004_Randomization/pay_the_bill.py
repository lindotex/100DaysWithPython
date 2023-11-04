# Who will pay the bill?
# You will write a code, that is going to get a random name on a list. The selected person will have to pay for everybody's food bill.
# You're not allowed to use the "choice()" function!
import string

# My attempt:
names_string = ["Angela", "Ben","Jenny", "Michael", "Chloe"]

names = names_string.split(", ")

import random

#Geting the total number of items in list
num_itens = len(names)
#Generating a random number between 0 and the last index of the list.
random_choice = random.randint(0, num_itens - 1)
# Selecting a random person from the list of names using random number.
paying_person = names[random_choice]

print(f"{paying_person} is going to pay the meal today!")
