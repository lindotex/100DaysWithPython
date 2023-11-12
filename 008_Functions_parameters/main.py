
# Functions:
def greed():
    print("Hello")
    print("How do you do")
    print("Isn't the weather nice today?")
    
greed()

# Functions with inputs
def greet_with_name(name):
    print(f"Hello, {name}!")
    print(f"How do you do{name}?")

greet_with_name("Alisson")

# Functions with multiple inputs

def greet_with(name, location):
    print(f"Hello, {name}")
    print(f"welcome to {location}!")

greet_with("Alisson", "Wonderland")

# Functions with keywords arguments:
greet_with(location="Barcelona", name="John")
    