from turtle import Turtle
from ball import Ball

class Paddle(Turtle):
    def __init__(self, ball:Ball):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 3)
        self.penup()
        self.x = 101
        self.ball = ball
        self.start = False
        self.goto(0, -185) 

    def left(self):
        new_x = self.xcor() - 20

        if new_x > -380:
            self.goto(x=new_x, y = self.ycor())
            if not self.start:
                new_x = self.ball.xcor() - 20
                self.ball.goto(x=new_x, y = self.ball.ycor())

    def right(self):
        new_x = self.xcor() + 20

        if new_x < 380:
            self.goto(x=new_x, y = self.ycor())
            if not self.start:
                new_x = self.ball.xcor() + 20
                self.ball.goto(x=new_x, y = self.ball.ycor())


    def release_ball(self):
        self.start = True
        self.ball.go_to_right()