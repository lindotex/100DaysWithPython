class Animal:
    def __init__(self, name):
        self.num_eyes = 2
        self.name = name

    def breathe(self):
        print(f"{self.name} is breathing.")
        
    def speak(self):
        print(f"{self.name} is trying to say something...")