# this is the ball class
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_distance = 10
        self.y_distance = 10
        self.ball_speed = 0.1

    def move(self):
        x_pos = self.xcor() + self.x_distance
        y_pos = self.ycor() + self.y_distance
        self.goto(x_pos, y_pos)

    def bounce_ball_y(self):
        self.y_distance *= -1

    def bounce_ball_x(self):
        self.ball_speed *= 0.9
        self.x_distance *= -1

    def position_reset(self):
        self.home()
        self.ball_speed = 0.1  # reset the speed after a miss
        self.bounce_ball_x()


