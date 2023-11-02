### Create a program using maths and f-String that
### tell us how many weeks we have left, if we live
### until 90 years old.
### It will take your age at an input, and show at
### the screen a message: "You have X weeks left"

age_now = input("How old are you?")
limit_age = 90

weeks = ((limit_age - int(age_now))*52)

print(f"You have {weeks} weeks left")