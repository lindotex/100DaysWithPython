import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
t.speed('fastest')

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color
    
def dawn_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + size_of_gap)
     
dawn_spirograph(5)

screen = t.Screen()
screen.exitonclick()
 
    
    