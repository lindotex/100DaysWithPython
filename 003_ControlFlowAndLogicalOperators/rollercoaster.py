print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
age = int(input("How old are you?"))

if height >= 120:
    print("You can ride the rollercoaster!")
    if age <= 18:
        print("Please, pay $7.00 to enter")
    else:
        print("Please, pay $12.00 to enter.")
    
else:
    print("You can not ride the rollercoaster yet...")