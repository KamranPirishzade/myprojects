from turtle import Turtle, Screen
from paddle import Padle
from ball import Ball
import time
from scoreboard import Score

screen=Screen()
screen.title("Pong game")
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.tracer(0)



paddle_r = Padle(cor_x=350, cor_y=0)
paddle_l=Padle(cor_x=-350, cor_y=0)
ball=Ball()
score=Score()



speed=0.1
game_is_con=True
while game_is_con:

    time.sleep(speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if ball.distance(paddle_r)<50 and ball.xcor()>320 or ball.distance(paddle_l)<50 and ball.xcor()<-320:

        speed*=0.9
        ball.bounce_x()
        ball.speed(speed)
    if ball.xcor()>380:
        ball.goto(0,0)
        ball.bounce_x()
        score.l_score()
        speed=0.1
    if ball.xcor()<-380:
        ball.goto(0,0)
        ball.bounce_x()
        score.r_score()
        speed=0.1


screen.exitonclick()
