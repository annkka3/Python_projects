from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PING PONG GAME')
screen.tracer(0)

r_paddle = Paddle(360, 0)
l_paddle = Paddle(-360, 0)
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 's')
screen.onkey(l_paddle.down, 'x')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()


    #detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or(ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()
        ball.increase_speed()

    #detect when right paddle missed the ball
    if ball.xcor() > 370:
        ball.reset_position()
        score.l_point()
        ball.original_speed()

    # detect when left paddle missed the ball
    if ball.xcor() < -370:
        ball.reset_position()
        score.r_point()
        ball.original_speed()

    if score.r_score == 5:
        game_is_on = False
        score.game_over_r()

    if score.l_score == 5:
        game_is_on = False
        score.game_over_l()







screen.exitonclick()