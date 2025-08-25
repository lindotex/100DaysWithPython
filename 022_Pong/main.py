import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score

#  Instances
# setup the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()
# setup the ball
ball = Ball()

# Paddle 1
paddle1 = Paddle((-360,0))
# Paddle 2
paddle2 = Paddle((360,0))

# Key bindings - Paddle 1
screen.onkey(paddle1.up,"w")
screen.onkey(paddle1.down,"s")

# Key bindings - Paddle 2
screen.onkey(paddle2.up,"Up")
screen.onkey(paddle2.down,"Down")

# setup the score
score1 = Score((-260, 260))
score2 = Score((260, 260))


# Game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.04)
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