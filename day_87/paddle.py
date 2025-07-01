from turtle import Turtle
from ball import Ball

class Paddle(Turtle):
    def __init__(self, ball:Ball):
        super().__init__()
        self.shape("square")
        self.shapesize(0.5, 3)
        self.penup()
        self.x = 101
        self.ball = ball
        self.start = False
        self.move_distance = 20
        self.goto_start_pos()
    
    def goto_start_pos(self):
        self.goto(0, -185) 

    def left(self):
        new_x = self.xcor() - self.move_distance

        if new_x > -380:
            self.goto(x=new_x, y = self.ycor())
            if not self.start:
                new_x = self.ball.xcor() - self.move_distance
                self.ball.goto(x=new_x, y = self.ball.ycor())

    def right(self):
        new_x = self.xcor() + self.move_distance

        if new_x < 380:
            self.goto(x=new_x, y = self.ycor())
            if not self.start:
                new_x = self.ball.xcor() + self.move_distance
                self.ball.goto(x=new_x, y = self.ball.ycor())


    def release_ball(self):
        self.start = True
        self.ball.go_to_right()