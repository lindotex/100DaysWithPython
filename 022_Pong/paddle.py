from turtle import Turtle

# Paddle class for Pong game

# Attributes
DOWN = 270
SPEED = 5
UP = 90
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

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_position = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_position)
        if self.segments:
            self.forward(SPEED)
            
    def up(self):
        if self.heading() != DOWN:
            self.setheading(UP)
    
    def down(self):
        if self.heading() != UP:
            self.setheading(DOWN)