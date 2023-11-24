from random import randint
from art import logo
want_play = True

cards = ["A", "2", "3", "4", "5","6","7","8","9","10","j","q","k"]
values = [11, 2,3,4,5,6,7,8,9,10,10,10,10]

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
    
    def add_another_number():
        hand.append(randomize())

    def verifying_input():
        """Verification of input
            Returns:
                Returns if it was typed (y) or (n) correctly.
        """
        answer = ""
        play_answer = False
        while play_answer == False:
            answer = input("Would you like to play Blackjack?\n Yes (y) or No (n)?:")
            if answer == "y" or answer == "n":
                play_answer = True
            else:
                print("Invalid answer, please type 'y' or 'n'.")
    
    verifying_input()
    
    if verifying_input().answer == "y":
        
        hand = [randomize(), randomize()]
        
        hand_cards =hand[0,0]
        hand_value = hand[1,1]
        
        enemy = [randomize(), randomize()]

        enemy_cards = enemy[0,0]
        enemy_value = enemy[1,1]

        print(f" Your cards are {hand_cards}, that values {hand_value}")
        print(f" Your enemy's cards are {enemy_cards}, that values {enemy_value}")
    
    if verifying_input().answer == 'n':
        want_play = False




