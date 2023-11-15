from art import logo
import os
# from reprlib import clear

print(logo)
print("Blind Bet Program")

end_bets = False
bets = {}

def clear():
    os.system("cls || clear")

def find_bigger_bet(bet_record):
    highest_bid = 0
    winner = ""
        
    for bets in bet_record:
        bet_amount = bet_record[bets]
        if bet_amount > highest_bid:
            highest_bid = bet_amount
            winner = bets
    clear()
    print(logo)
    print(f"The winner is {winner} with a bid of €{highest_bid}")
    
while end_bets == False:
    name = input("Insert your name, please:\n")
    value = float(input("Insert your bid value, please: \n"))
    bets[name] = value
    more_bets = input("Is there any other bets to be made?\n Yes (y) or No (n):")
    
    if more_bets == 'n':
        end_bets = True
        find_bigger_bet(bets)
    elif more_bets == 'y':
        clear()
        print(logo)