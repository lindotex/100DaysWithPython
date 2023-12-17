from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape("turtle")
tim.color("orange")
def draw(sides):
    
    for _ in range (sides):
        angle = 360 / sides
        tim.forward(50)
        tim.right(angle)
        
for shape in range (3,11):
    colors = ['red','yellow','blue', 'green','purple']
    tim.color(random.choice(colors))
    draw(shape)
    
screen = Screen()
screen.exitonclick()

        