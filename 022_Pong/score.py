from turtle import Turtle

# Paddle class for Pong game
class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(position)
        self.score = 0
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 24, "normal"))
        
    def increase_score(self):
        self.score += 1
        self.update_score()