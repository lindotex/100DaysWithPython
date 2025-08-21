from animal import Animal

class Fish(Animal):
    def __init__(self, name, species):
        super().__init__(name)
        self.species = species
        self.num_eyes = 2  # Fish typically have two eyes
        
    def swim(self) -> None:
        print(f"{self.name} is swimming.")

    def breathe(self) -> None:
        super().breathe()
        print(f"{self.name} is breathing through gills.")

    def speak(self)-> None:
        super().speak()
        print(f"{self.name} makes a bubbling sound.")