

# How to proper work with Global variables:

enemies = 1 # Never modify this.

print(f"Enemies inside function: {enemies}")

def increase_enemies():
    global enemies # This is how you import a Global property from its program to work with inside a function.
    enemies += 1
    print(f"Enemies inside function: {enemies}")

increase_enemies() # Calling the function will make it increase the variable.
print(f"Enemies inside function: {enemies}")
increase_enemies()

##################### GLOBAL VARIABLES #########################
# They are better suitable for variables that must never change,
# such as constants ( pi = 3.14159 ).
# As convention, it should be named as full-capital-letters!
# For example: 
#               NUMBER_PI = 3.14159
#               URL = "https://blabla.bla"
#               TWITTER_HANDLE = "@lindotex"
#
#
################################################################