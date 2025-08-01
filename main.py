from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import  time
from  scoreboard import Scoreboard
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong game")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball=Ball()
scoreboard = Scoreboard()

# Keyboard bindings
screen.listen()



screen.onkey(r_paddle.go_up, 'Up')     # Use onkey, not onclick
screen.onkey(r_paddle.go_down, 'Down')     # Use onkey, not onclick
screen.onkey(l_paddle.go_up, 'w')     # Use onkey, not onclick
screen.onkey(l_paddle.go_down, 's')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    if ball.xcor() > 380:
        ball.reset()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset()
        scoreboard.r_point()

screen.exitonclick()
