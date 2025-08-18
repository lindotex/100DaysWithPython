from turtle import Screen
from snake import Snake  # Import the Snake class from snake.py
import time

#  Initialize the screen
screen = Screen();
screen.setup(width=600, height=600);
screen.bgcolor("black");
screen.title("Snake Game");
screen.tracer(0)  # Turns off the screen updates

#  Main game loop
snake = Snake()

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


screen.exitonclick()