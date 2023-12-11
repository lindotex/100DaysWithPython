class Animals():
    def __init__(self, name, color, legs):
        self.id = id
        self.name = name
        self.scream = ''
        self.color = color
        self.legs = legs
    
    def roar(self, scream):
        self.scream = scream

        
class Dog(Animals):
    def walk(self):
        print(f"{self.name} is walking")
        

Buggy = Dog(name='Buggy',legs=4, color='brown')
Tom = Dog(name='Tom',legs=3, color='purple')

Buggy.walk()

print(f"{Tom.name} is a Dog, he has {Tom.legs} legs. He is a {Tom.color} color Dog.")