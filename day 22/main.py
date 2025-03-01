from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.setup(width=800, height=400)
screen.tracer(0)

ball = Ball()

for i in range(0, 20):
    line = Turtle("square")
    line.penup()
    line.shapesize(stretch_wid=0.5, stretch_len=0.1)
    line.setpos(0 , (212 - (i + 1) * 20))

paddle_1 = Paddle(350, 0)
paddle_2 = Paddle(-350, 0)


screen.listen()
screen.onkey(paddle_1.move_up, 'Up')
screen.onkey(paddle_1.move_down, 'Down')
screen.onkey(paddle_2.move_up, 'w')
screen.onkey(paddle_2.move_down, 's')


game_state = True

while game_state:
    screen.update()
    screen.delay(1)
    ball.move()

    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.bounce_y()
        
    if ball.distance(paddle_1) < 50 and ball.xcor() > 340 or ball.distance(paddle_2) < 50 and ball.xcor() > -360:
        ball.bounce_x()

screen.exitonclick()