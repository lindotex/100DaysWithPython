################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Enemies inside the function acts only in scope of its function, not modifying the property outside of its function.

###### How does Scope Works:

variable = 'x'

def another_variable():
    variable = 'y'
    return variable

    
class Other_variable:
    variable = 'z'

"""
    Although they're named as the same variable 'variable', print each of them will reveal that they are under different scopes.
        - Variable: Outside of everything, at root of Main.
        - another_variable(): inside a function.
        - Other_variable.variable: Inside a class.
"""
print(variable)
print(another_variable())
print(Other_variable.variable)

# Local Scope:

def drink_potion():
    """ Function that heals a character """
    potion_strength = 2 # defining variable
    print(potion_strength) # this will work

print(potion_strength) 
# This will not work, 'cause it is outside of its scope.  potion_strength is declared inside the function, so it can only work inside of it.


# Global Scope:

player_health = 10 # Variable declared at root, so, it is a global variable.

def drinking_potion():
    potion_strength = 2 # Property in the scope of function. So it have a Local Scope.
    print(player_health) # It will work, 'cause it is defined globally, outside of the function.

drinking_potion()