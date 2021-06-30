from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# setting up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("The Pong Game")

# to set up everything behind the scenes
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

ball = Ball()

score = Scoreboard()
# to enable use of arrow keys
screen.listen()
screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

# loop to play the game
game_on = True

while game_on:
    # show the screen again
    screen.update()
    ball.move()
    time.sleep(ball.ball_speed)  # slow down the ball movement a bit

    # check if ball hits top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_ball_y()

    # detect collision of ball with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_ball_x()

    # detect when paddle misses the right paddle
    if ball.xcor() > 360:
        score.left_points()  # give opponent score
        ball.position_reset()

    # detect when paddle misses the left paddle
    if ball.xcor() < -360:
        score.right_points()  # give opponent score
        ball.position_reset()


screen.exitonclick()
