from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=800, height=400)

ball = Turtle("square")

for i in range(0, 20):
    line = Turtle("square")
    line.penup()
    line.shapesize(stretch_wid=0.5, stretch_len=0.1)
    line.setpos(0 , (212 - (i + 1) * 20))


class Paddle():
    def __init__(self):
        self.padle_list = []
        self.create_paddle()
    
    def create_paddle(self):
        for i in range(0, 4):
            line = Turtle("square")
            line.penup()
            line.setpos(-390 , (40 - (i + 1) * 20))
            self.padle_list.append(line)

    def move_up(self):
        for item in self.padle_list:
            item.setpos(-390, item.ycor() + 20)
    
    def move_down(self):
        for item in reversed(self.padle_list):
            item.setpos(-390, item.ycor() - 20)


paddle = Paddle()

screen.listen()
screen.onkey(paddle.move_up, 'Up')
screen.onkey(paddle.move_down, 'Down')

screen.exitonclick()