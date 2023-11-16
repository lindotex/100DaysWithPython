def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False



# TODO: Add more code here 👇
def days_in_month(year, days):
    month_days =  [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if month < 0 or month > 12:
        return f"There is no month {month}... type a valid word."
    if is_leap(year) == True and month == 2:
        return 29
    else:
        return month_days[month -1 ]
    
  
#🚨 Do NOT change any of the code below 

year = int(input("Type the Year:\n")) # Enter a year
month = int(input("Type the month: \n")) # Enter a month
days = days_in_month(year, month)
print(days)