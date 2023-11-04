# Pizza order Program:

#my answer
bill = 0

print("Welcome to Pizza's place, what size of pizza would you like?")
answer = input("small, medium or large: S, M, L.")

if answer == "s":
    bill += 15
    answer2 = input("would you like to add Peperony for $2? Y or N ?")
    if answer2 == "Y":
        bill = bill + 2
        
elif answer == "m":
    bill += 20
    answer2 = input("would you like to add Peperony for $3? Y or N ?")
    if answer2 == "Y":
        bill = bill + 3
else: 
    bill += 25
    answer2 = input("would you like to add Peperony for $3? Y or N ?")
    if answer2 == "Y":
        bill = bill + 3
        
plus_cheese = input("Would you like to add cheese? Y or N")

if plus_cheese == "Y":
    bill = bill + 1

print(f"Thank you, your final bill is {bill}")


# CORRECTION:

bill = 0

print("Welcome to Pizza's place, what size of pizza would you like?")
size = input("small, medium or large: S, M, L.")

if size == "s":
    bill += 15        
elif size == "m":
    bill += 20
else: 
    bill += 25
    
add_peperoni = input("Would you like to add Peperoni? Y or N")
if add_peperoni == "Y":
    if size == "s":
        bill += 2
    else:
        bill +=3

add_cheese = input("Would you like to add cheese? Y or N")

if add_cheese == "Y":
    bill += 1

print(f"Thank you, your final bill is {bill}")