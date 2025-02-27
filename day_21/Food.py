from turtle import Turtle
import random as r

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('blue')
        self.refresh()
        
    
    def refresh(self):
        x = r.randint(-270, 270)
        y = r.randint(-270, 270)
        self.goto(x, y)