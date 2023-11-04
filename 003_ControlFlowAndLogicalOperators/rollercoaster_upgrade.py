# ROllercoaster Upgrade.
# Would you like to take pictures?

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?"))
age = int(input("How old are you?"))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    if age <= 12:
        print("Child, pay $5.00 to enter")
        bill = 5
    elif age < 18:
        print("Youth, pay $7.00 to enter.")
        bill = 7
    else:  
        print("Adult, pay $12.00 to enter.")
        bill = 12
    whants_photo = bool(input("Do you wanna photo taken? Y or N"))
    if whants_photo == "y":
        bill = bill + 3
        print("Your Photo has been taken, your Bill is ${bill}")
    else:
        print("Your Photo hasn't been taken, your Bill is ${bill}")
else:
    print("You can not ride the rollercoaster yet...")