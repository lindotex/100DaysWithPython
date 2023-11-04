# Leap year calculator:

#my answer
year = int(input("Type an specific year:"))

year_by_four = year % 4
year_by_hundred = year % 100
year_by_four_hundred = year % 400

if year_by_four == 0:
    leap_year = True
elif year_by_four_hundred == 0:
    leap_year = True
elif year_by_four_hundred == 0:
    leap_year = True
else:
    leap_year = False

if leap_year == True    
    print(f"The selected Year is a Leap Year")
else:
    print(f"The selected Year is not a Leap Year")
    
# Teacher's Answer:
year = int(input())

if year % 4 == 0
    if year % 100 == 0
        if year % 400 == 0
            print("Leap Year")
        else:
            print("Not Leap Year")
    else: 
        print("Leap Year")
else: 
    print("Not Leap Year")
        