from turtle import Screen
from snake import Snake  # Import the Snake class from snake.py
from food import Food  # Import the Food class from food.py
from scoreboard import Scoreboard  # Import the Scoreboard class from scoreboard.py

import time
# import random

#  Initialize the screen
screen = Screen();
screen.setup(width=600, height=600);
screen.bgcolor("black");
screen.title("Snake Game");
screen.tracer(0)  # Turns off the screen updates

#  Main game loop
snake = Snake()
food = Food()  # Create an instance of the Food class
scoreboard = Scoreboard()  # Create an instance of the Scoreboard class

# Keys to control the snake
screen.listen()
screen.onkey(snake.up, "Up")  # Bind the Up arrow key to move the snake
screen.onkey(snake.down, "Down")  # Bind the Down arrow key to move the snake
screen.onkey(snake.left, "Left")  # Bind the Left arrow key to move the snake
screen.onkey(snake.right, "Right")  # Bind the Right arrow key to move


game_is_on = True

while game_is_on:   
    # Update the screen
    screen.update()
    time.sleep(0.1)

    snake.move()  # Call the move method of the Snake class

    # collision with food
    if snake.head.distance(food) < 15:  # Check if the snake's head is close to the food
        scoreboard.increase_score()  # Increase the score
        food.refresh()
        scoreboard.update_scoreboard() 
        snake.extend()  # Call the extend method of the Snake class to grow the snake
        
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    
    # Detect collision with tail
    for segment in snake.segments[1:]:  # Exclude the head segment
        if snake.head.distance(segment) < 10:  # Check if the head collides with any segment of the tail
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()