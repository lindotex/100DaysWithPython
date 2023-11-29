number = int(input()) # Which number do you want to check?

if number % 2 == 0: ### FIX: Use == instead of =
  print("This is an even number.")
else:
  print("This is an odd number.")


##################################

# Which year do you want to check?
year = int(input()) ## FIX: Convert it into inter.

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
  

###################################

target = int(input())
for number in range(1, target + 1):
  if number % 3 == 0 and number % 5 == 0: ## FIX: changed or for changed
    print("FizzBuzz")
  if number % 3 == 0: ## Use ELIF, insteado of If-else.
    print("Fizz")
  if number % 5 == 0:  ## Use ELIF, insteado of If-else.
    print("Buzz")
  else:
    print([number]) ## FIX: Remove the square  brackets