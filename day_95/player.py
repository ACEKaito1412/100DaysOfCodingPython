from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(0.5, 3)
        self.penup()
        self.move_distance = 20
        self.go_to_start()

    def go_to_start(self):
        self.goto(0, -180)


    def left(self):
        new_x = self.xcor() - self.move_distance

        if new_x > -380:
            self.goto(x = new_x, y = self.ycor())

    def right(self):
        new_x = self.xcor() + self.move_distance

        if new_x < 380:
            self.goto(x = new_x, y = self.ycor())
        

    def shoot(self):
        pass