import time
from turtle import Screen
from paddle import Paddle

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

screen.listen()

# Paddle 1
paddle1 = Paddle((-360,0))
screen.onkey(paddle1.up,"w")
screen.onkey(paddle1.down,"s")

# Paddle 2
paddle2 = Paddle((360,0))
screen.onkey(paddle2.up,"Up")
screen.onkey(paddle2.down,"Down")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
screen.exitonclick()    