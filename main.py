# pong game (Day- 22):


from turtle import Screen
from paddle import Paddle
from scoreboard import ScoreBoard
import time
import ball

screen = Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.listen()
screen.setup(width=800, height=600)
screen.tracer(0)


l_paddle = Paddle(-370, 0)
r_paddle = Paddle(370, 0)
ball = ball.Ball()
scoreboard = ScoreBoard()

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)

    # moving the ball
    ball.start_right()

    # bouncing the ball
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # if r paddle misses
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.l_point()

    # if l paddle misses
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
