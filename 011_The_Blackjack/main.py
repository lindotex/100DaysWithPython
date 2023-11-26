############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

#################### MY ATTEMPT ########################
# from random import randint
# from art import logo
# want_play = True

# cards = ["A", "2", "3", "4", "5","6","7","8","9","10","j","q","k"]
# values = [11, 2,3,4,5,6,7,8,9,10,10,10,10]

# GAME START
# print(logo)
# player_hand = []
# computer_hand = []

# def randomize():
#     """Randomize
#         Args:
#             card (array): Array of Cards
#             values (array): Array of Values
#         Returns:
#             returns a random card and its value.
#     """
#     random = int(randint(1,12))
#     random_card = cards[random]
#     random_value = values[random]
    
#     return(random_card, random_value)

# def add_another_number(array):
#     """add_another_number
#         Args:
#             array (array): input of array
#         Returns:
#             insert a random card at array
#     """
#     array.append(randomize())

# def verifying_input():
#     """Verification of input
#         Returns:
#             Returns if it was typed (y) or (n) correctly.
#     """
#     answer = ""
#     play_answer = False
#     while play_answer == False:
#         answer = input("Would you like to play Blackjack?\n Yes (y) or No (n)?:")
#         if answer == "y" or answer == "n":
#             play_answer = True
#         else:
#             print("Invalid answer, please type 'y' or 'n'.\n")
    
#     if answer == 'n':
#         print("Thank you!\nBye Bye!")
#     return answer

# if verifying_input() == 'y':
#     player_hand = [randomize(), randomize()]
#     computer_hand = [randomize(), randomize()]

#     hand_cards = [player_hand[0][0], player_hand[1][0]]
#     hand_value = [player_hand[0][1], player_hand[1][1]]

#     enemy_cards = computer_hand[0][0]
#     enemy_value = computer_hand[0][1]

#     hand_sum = (player_hand[0][1] + player_hand[1][1])
#     enemy_sum = (computer_hand[0][1] + computer_hand[1][1])

#     print(f" Your cards are {hand_cards}, that values {hand_value}, as total {hand_sum}.")
#     print(f" Your enemy's first cards is {enemy_cards}, that values {enemy_value}.\n")

# def verify_winner():
#     draw_new_card = ''
#     if hand_sum > 21 and enemy_sum < 21:
#         draw_new_card = print(f"Your hand is out limits, {hand_sum}... You loose.")

#     if hand_sum == 21 and enemy_sum < 21:
#         draw_new_card = print(f"BLACKJACK! Your WON!\n, {hand_sum}... It is a perfect score.")

#     if enemy_sum > 21 and hand_sum < 21:
#         draw_new_card = print(f"Your WON!\n, Your enemy has more than 21 on his hand.")

#     if enemy_sum == 21 and hand_sum < 21: 
#         draw_new_card = print(f"You loose,\n Your enemy has complete 21.")
        
#     if enemy_sum == 21 and hand_sum == 21: 
#         draw_new_card = print("WOW...\n it is a draw! \n Both of you has achieved 21 points.")
        
#     if hand_sum < 21 and enemy_sum < 21:
#         draw_new_card = print(f"You still have some points to make,\nYou have {hand_sum}... It is missing {21 - hand_sum}.")
#         draw_new_card = input("Would you like to draw another card?\n Yes (y) or No (n):")
#     return draw_new_card
        
# def winner():
#     if hand_sum > enemy_sum:
#         print(f"You WON!\n You have {hand_sum} points, your enemy has only {enemy_sum}.")
#     elif enemy_sum > hand_sum:
#         print(f"You loose!\n You have {hand_sum} points, your enemy has {enemy_sum}, he Won.")
        
# if verify_winner() == 'y':
#     print('We will play again.................')
# else:
#     winner()

# want_play = True
# while want_play == True:
    
#     if verifying_input() == 'n':
#         want_play = False
#################### MY ATTEMPT ########################


################################### CORRECTION ##############################################
from art import logo
import random
import os

user_card = []
computer_card = []
cards = [11, 2,3,4,5,6,7,8,9,10,10,10,10]

"""Returns a random card from the deck"""
def deal_card():
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return its sums"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)    
    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Computer Has Blackjack!\nYou Lose...."
    elif user_score == 0:
        return "You Win!!!\nYou have Blackjack!"
    elif user_score > 21:
        return "You Lose...\nYou have reached more than 21 points."
    elif computer_score > 21:
        return "You WON!!! \nComputer have reached more than 21 points."
    elif user_score > computer_score:
        return "You Win!!!\nYou has more points than the Opponent"
    else:
        return "You Lose... \nYour Opponent has more points than you..."

def play_game():
    print(logo)
    is_game_over = False
    """ Giving 2 cars for player and computer """
    for _ in range(2): 
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not is_game_over:
            
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"Your hand: {user_card}. Sums: {user_score}\nYour enemy first card: {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Would you like to draw another card?\nYes(y) or No(n):")
            if user_should_deal == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True
        
    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)       

    print(compare(user_score,computer_score))
    print(f"You cards: {user_card} and the Opponent: {computer_card}")
    print(f"You has scored {user_score} and the Opponent has {computer_score}")

while input("Do you want to play a game of Blackjack?\nType Yes(y) or No(n):") == 'y':
    os.system('clear')
    user_card = []
    computer_card = []
    play_game()