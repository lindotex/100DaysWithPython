from turtle import Turtle
import random

class Food (Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.speed("fastest")
        self.refresh()  # Place the food at a random position when initialized
        
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)