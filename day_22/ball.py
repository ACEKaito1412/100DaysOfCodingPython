from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.x_trajectory = -1
        self.y_trajectory = -1
        self.cur_speed = 0.000001
        self.start()
    
    def move(self):
        new_y = self.y_trajectory
        new_x = self.x_trajectory

        self.goto(self.xcor() + new_x, self.ycor() + new_y)

    def bounce_x(self):
        self.x_trajectory *= -1
        self.cur_speed *= 0.9

    def bounce_y(self):
        self.y_trajectory *= -1

    def start(self):
        self.cur_speed = 0.000001
        self.goto(0,0)

    
    def go_to_right(self):
        self.x_trajectory = 1
        self.y_trajectory = 1
    
    
    def go_to_left(self):
        self.x_trajectory = -1
        self.y_trajectory = -1
