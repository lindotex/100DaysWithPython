# Love Calculator:

print("The love calculator is calculating your score!")
name1 = input("What is your name?")
name2 = input("What is the name of your lover?")

# changin all letters to lower case:
combined_names = name1 + name2
lower_names = combined_names.lower()

#counting the number of times that letters repeats
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

# sum the score
score = int(str(first_digit) + str(second_digit))

# Analizing the results:

if (score < 10) or (score > 90):
    print(f"Your score is {score}, you're like coke and mentos")
elif (score >=40) and (score<=50):
    print(f"Your score is {score}, you're fine together")
else:
    print(f"Your score is {score}.")
    