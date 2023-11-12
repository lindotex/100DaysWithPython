def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Is a prime Number")
    else:
        print("Isn't a prime Number ")

n = int(input("witch number do you want to test?"))
prime_checker(number=n)