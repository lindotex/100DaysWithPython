import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

screen = Screen()
ball = Ball()
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

score1 = Score((-260, 260))
score2 = Score((260, 260))

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    
    
    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # Detect collision with paddle
    if (ball.distance(paddle1) < 50 and ball.xcor() < -320) or (ball.distance(paddle2) < 50 and ball.xcor() > 320):
        ball.bounce_x()
        
    # Detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_position()  
        score1.increase_score()
    if ball.xcor() < -380:
        ball.reset_position()  
        score2.increase_score()
    
    
screen.exitonclick()    