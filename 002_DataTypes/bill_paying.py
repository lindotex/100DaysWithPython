#Exercices
# My trying exercice 
bill = print(input('What was the total bill?'))
total_people = print(input('How many people to split the bill?'))
percentage = print(input('What percentage tip would you like to give? 10, 12 or 15?'))

total = (float(bill) + ((float(bill)*float(percentage))/100))/float(total_people)
print(f'Each person will pay $ {total}')

# Correct answer:
print("Welcome to the tip calculator!")
bill = float(input("What was the bill?"))
tip = float(input("How much tips would you like to give? 10? 12? 15?"))
people = int(input("How many people are paying?"))
bill_with_tip = tip/100 * bill + bill

bill_per_person = bill_with_tip /people

final_amount = round(bill_per_person, 2) #Will not show int if are 0
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay ${final_amount}")
