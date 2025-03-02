from turtle import Turtle
class Paddle(Turtle):

    def __init__(self, x , y):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.x = x
        self.goto(x = x, y = y)


    def move_up(self):
        new_y = self.ycor() + 20
        if new_y < 180:
            self.goto(self.x, new_y)
    
    def move_down(self):
        new_y = self.ycor() - 20
        if new_y > -180:
            self.goto(self.x, new_y)
