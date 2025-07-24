from turtle import Turtle

class Bullet(Turtle):
    def __init__(self, direction:bool, x_pos, y_pos):
        super().__init__()
        self.shape('square')
        self.shapesize(0.05, 0.05)
        self.penup()
        self.move_speed = 10
        # true :up false:down
        self.direction = direction
        self.goto(x_pos, y_pos)
        self.move_towards()
        
    
    def move_towards(self):
        if self.direction:
            new_y = self.ycor() + (self.move_speed * 1)
        else:
            new_y = self.ycor() + (self.move_speed * -1)

        self.goto(x = self.xcor(), y = new_y)