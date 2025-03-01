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
        self.goto(self.x, self.ycor() + 20)
    
    def move_down(self):
        self.goto(self.x, self.ycor() - 20)
