from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

# Scoreboard class to keep track of the score and high score
# It inherits from Turtle to use turtle graphics for displaying the score
# It also handles saving and loading the high score from a file
# The scoreboard is displayed at the top of the screen
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.load_high_score()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_scoreboard()

    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0

    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

