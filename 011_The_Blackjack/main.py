from random import randint
from art import logo
want_play = True

cards = ["A", "2", "3", "4", "5","6","7","8","9","10","j","q","k","a"]
values = ['', 2,3,4,5,6,7,8,9,10,10,10,10,""]

# GAME START
print(logo)
hand = []

def randomize():
    """Randomize
        Args:
            card (array): Array of Cards
            values (array): Array of Values
        Returns:
            returns a random card and its value.
    """
    random = int(randint(1,13))
    random_card = cards[random]
    random_value = values[random]
    
    return(random_card, random_value)

while want_play == True:
    play_answer = False
    while play_answer == False:
        answer = input("Would you like to play Blackjack?\n Yes (y) or No (n)?:")
    
        if answer == "y" or answer == "n":
            play_answer = True
        else:
            print("Invalid answer, please type 'y' or 'n'.")
        
    if answer == 'n':
        want_play = False
    
    hand_1 = randomize()
    hand_2 = randomize()
    
    hand = [hand_1[0], hand_2[0]]
    hand_value = hand_1[1] + hand_2[1]

    print(f" Your card is {hand}, that values {hand_value}")



