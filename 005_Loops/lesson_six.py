# FizzBuss game
# divisible by 3 = Fizz
# divisible by 5 = Buzz
# divisible by 3 and 5 = FizzBuzz

x = int(input("Digite um limite:"))

count = 0
for number in range(1, x + 1):
    count+= number
    if number % 3 == 0 and number %5 == 0:
        print(f"{number} FizzBuzz")
    elif number % 3 == 0:
        print(f"{number} Fizz")        
    elif number % 5 == 0:
        print(f"{number} Buzz")
    else:
        print(f"{number} !")
        
