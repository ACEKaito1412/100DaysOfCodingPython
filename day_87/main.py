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
from bricks import Bricks
from scoreboard import ScoreBoard


screen = Screen()
screen.setup(width=800, height=400)
screen.tracer(0)


ball = Ball()
padle = Paddle(ball)
bricks = Bricks()
score = ScoreBoard()


screen.listen()
screen.onkey(padle.right, "Right")
screen.onkey(padle.left, "Left")
screen.onkey(padle.release_ball, "Up")

game_state = True
ball_bounce_state = False

while game_state:
    screen.update()
    score.update_scoreboard()
    time.sleep(ball.cur_speed)

    if padle.start:
        ball.move()
        bricks.check_collision(ball=ball, score=score)
        
        if bricks.check_available_bricks():
            score.level += 1
            ball.cur_speed *= 0.09
            padle.move_distance += 5
            padle.start = False
            bricks.show_all_bricks()
            ball.start()
            padle.goto_start_pos()

        if ball.ycor() > 180:
            ball.bounce_y()
        elif ball.xcor() > 380 or ball.xcor() < -380:
            ball.bounce_x()
    
        # 50 >= -50 and -50 <= 70
        if (padle.xcor() - 50 <= ball.xcor() <= padle.xcor() + 50):
            print("hello")
        # 5
        # -10 => 5 <= 10
        if ball_bounce_state == False: 
            if (padle.xcor() - 50 <= ball.xcor() <= padle.xcor() + 50) and ball.ycor() < -175:
                ball_bounce_state = True
                print("Called")
                ball.bounce_y()

        print(f"{ball.ycor()} >= {padle.ycor()} state: {ball_bounce_state}")
        if ball.ycor() == 0:
            ball_bounce_state = False

        if ball.ycor() < -195:
            bricks.remove_all_bricks()
            bricks.show_all_bricks()
            padle.start = False
            padle.goto_start_pos()
            score.level = 1
            score.score = 0
            ball.cur_speed = 0.01
            padle.move_distance = 20
        





screen.tracer(1)
screen.exitonclick()