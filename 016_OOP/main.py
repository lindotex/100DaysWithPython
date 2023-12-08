from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

# part one : print reports
coffee_maker.report()
money_machine.report()

def off():
    print("Your Machine is turning off.")
    print('[..........]')
    time.sleep(1)
    print('[|||.......]')
    time.sleep(1)
    print('[||||||....]')
    time.sleep(1)
    print('[|||||||||.]')
    time.sleep(1)
    print('[||||||||||]')
    time.sleep(1)
    print("Your Machine has been turned off.")

while is_on:
    options = menu.get_items()
    
    choice = input(f'What would you like?\n{options}:\n')
    
    if choice not in ['off', 'report', 'latte', 'cappuccino', 'espresso']:
        print('please, insert a valid option.')
    
    elif choice == 'off':
        off()
        is_on = False
    
    elif choice == 'report':
        coffee_maker.report()
        money_machine.report()
    
    else:
        drink = menu.find_drink(choice)
        # part two : Check if resources are enough to prepare the beverage.
        # parte three :  process coins.
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            time.sleep(1)
            coffee_maker.make_coffee(drink)