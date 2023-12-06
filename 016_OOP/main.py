from prettytable import PrettyTable
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
menu = Menu()
coffee = MenuItem('coffee',80,0,12,1.99)
money_machine = MoneyMachine()

print(coffee.cost)
