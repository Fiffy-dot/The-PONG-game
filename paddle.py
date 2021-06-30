# this is the paddle class file
from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    # methods for moving up and down
    def move_up(self):
        y_pos = self.ycor() + 20
        self.goto(self.xcor(), y_pos)

    def move_down(self):
        y_pos = self.ycor() - 20
        self.goto(self.xcor(), y_pos)
