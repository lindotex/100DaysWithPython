import time
from turtle import Screen
from paddle import Paddle

screen = Screen()
paddle1 = Paddle((-360,0))
paddle2 = Paddle((360,0))

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


screen.listen()
screen.onkey(paddle1.up,"Up")
screen.onkey(paddle1.down,"Down")

game_is_on = True

while game_is_on:   
    # Update the screen
    screen.update()
    time.sleep(0.1)
    # time.sleep(0.1)   
    # paddle1.move()
    

screen.exitonclick()    