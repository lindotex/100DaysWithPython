

from lib import beverages, resources, coins

# GLOBAL
money = 0

def calculate(quarter, dime, nickel, penny):
    return (quarter*coins['quarter'])+(dime*coins['dime'])+(nickel*coins['nickel'])+(penny*coins['penny']) 

def compare(paid, price):
    if paid > price:
        return paid - price
    elif paid == price:
        return 0
    else:
        return f'missing € {paid - price}'

def prepare_coffee(beverage_type, credit, price):
    coffee_used = resources['coffee'] - beverages[beverage_type]['ingredients']['coffee']
    water_used = resources['water'] - beverages[beverage_type]['ingredients']['water']
    milk_used = resources['milk'] - beverages[beverage_type]['ingredients']['milk']
    
    if coffee_used and water_used and milk_used > 0:
        if credit >= price:
            print('Ok, your Beverage is being prepared...')
            print('Here you are!')
            print(f"Here is your change: € {round(compare(credit, price), 2)}")
        else:
            print("Can't be done...")
                 

option = str(input('What would you like ? (Espresso, Latte, Cappuccino):\n'))
print(f'You chose {option}, it will cost you {beverages[option]['price']}')
quarters = int(input("How many quarters (0.25)?:"))
dimes = int(input("How many dimes (0.10)?:"))
nickels = int(input("How many nickels (0.05)?:"))
pennies = int(input("How many pennies (0.01)?:"))

credit = calculate(quarters, dimes, nickels, pennies)

print(f"You paid €{round(credit,2)}.")
prepare_coffee(option, credit, beverages[option]['price'])