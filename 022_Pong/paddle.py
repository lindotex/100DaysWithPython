from turtle import Turtle

# Paddle class for Pong game
# Attributes
WIDTH = 1
HEIGHT = 4

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=HEIGHT, stretch_len=WIDTH)         
        self.penup()
        self.goto(position)
    
    def create_paddle(self):
        for position in position:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        
    def up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)
            
    def down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)