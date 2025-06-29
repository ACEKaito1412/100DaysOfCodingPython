# conditions 
    # game ends when ball wasnt catch three times
# paddle at bottom
    # move left and right
# moving ball
    # bounce at wall and the paddle
# bricks 
    # destroy when hit by ball

import time, random
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball


screen = Screen()
screen.setup(width=800, height=400)
screen.tracer(0)


ball = Ball()
padle = Paddle(ball)


screen.listen()
screen.onkey(padle.right, "Right")
screen.onkey(padle.left, "Left")
screen.onkey(padle.release_ball, "Up")

game_state = True

while game_state:
    screen.update()
    time.sleep(0.001)

    if padle.start:
        ball.move()
        if ball.ycor() > 180:
            ball.bounce_y()
        elif ball.xcor() > 380 or ball.xcor() < -380:
            ball.bounce_x()
    
        # 5
        # -10 => 5 <= 10
        if (ball.xcor() >= padle.xcor() - 10 and ball.xcor() <= padle.xcor() + 10) and ball.ycor() > -195:
            ball.bounce_y()
            # n = random.randint(0, 1)
            # print(n)
            # if n == 1:
            #     ball.go_to_left()
            # else:
            #     ball.go_to_right()



screen.tracer(1)
screen.exitonclick()