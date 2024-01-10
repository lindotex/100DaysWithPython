from turtle import Turtle, Screen
import random

tim = Turtle()

def random_color(): 
    return random.randint(0, 255)
    
# colors = ['red', 'blue', 'green', 'purple']
direction = [0,45,90,135,180,225,270, 315]
tim.pensize(15)

for _ in range(0,100):
    tim.color(random_color(),random_color(),random_color())
    tim.forward(50)
    tim.setheading(random.choice(direction))

screen = Screen()
screen.exitonclick()
 
    
    