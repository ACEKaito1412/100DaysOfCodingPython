from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.goto(0,0)
        self.x_trajectory = 1
        self.y_trajectory = 1
    
    def move(self):
        new_y = self.y_trajectory
        new_x = self.x_trajectory

        self.goto(self.xcor() + new_x, self.ycor() + new_y)

    def bounce_x(self):
        self.x_trajectory *= -1

    def bounce_y(self):
        self.y_trajectory *= -1