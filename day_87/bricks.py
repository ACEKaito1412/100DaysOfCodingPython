from turtle import *
from ball import Ball
from scoreboard import ScoreBoard

class Bricks():
    def __init__(self):
        self.brick = {}
        self.layers = 5
        self.top_start = 130
        self.create_bricks()

    def create_bricks(self):
        n_y = self.top_start
        for i in range(self.layers):
            start = -405
            array = []
            for j in range(15):
                n_x = start + 50
                n_brick = Brick(n_x, n_y)
                start += 50
                array.append(n_brick)
            n_y -= 20
            self.brick[i] = array

    def check_collision(self, ball:Ball, score:ScoreBoard):
        for key, value in self.brick.items():
            for item in value:
                if not item.isBroken:
                    if item.xcor() - 28 <= ball.xcor() <= item.xcor() + 28 and item.ycor() - 8 <= ball.ycor() <= item.ycor() + 8:
                        item.isBroken = True
                        item.hideturtle()
                        ball.bounce_y()
                        score.update_score(10)

    def check_available_bricks(self)->bool:
        for key, value in self.brick.items():
            for item in value:
                if not item.isBroken:
                    return False
                
        return True

    def remove_all_bricks(self):
        for key, value in self.brick.items():
            for item in value:
                if not item.isBroken:
                    item.isBroken = True
                    item.hideturtle()

    def show_all_bricks(self):
        for key, value in self.brick.items():
            for item in value:
                if item.isBroken:
                    item.isBroken = False
                    item.showturtle()

        return True



class Brick(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(0.3, 2)
        self.penup()
        self.goto(x, y)
        self.isBroken = False