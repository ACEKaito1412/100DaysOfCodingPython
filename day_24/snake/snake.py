from turtle import Turtle

UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_list = []
        self.state = "left"
        self.setup_snake()
        self.head = self.snake_list[0]

    def setup_snake(self):
        for i in range(0, 3):
            n = Turtle('square')
            n.penup()
            n.setpos(i * -20, 0)
            n.color('white')
            self.snake_list.append(n)

    def extend(self):
        self.add_segment(self.snake_list[-1].position())

    def add_segment(self, position):
        n = Turtle('square')
        n.penup()
        n.setpos(position)
        n.color('white')
        self.snake_list.append(n)

    def move(self):
        for index in range(len(self.snake_list) - 1, 0, -1):
            x = self.snake_list[index - 1].xcor()
            y = self.snake_list[index - 1].ycor()
            self.snake_list[index].goto(x, y)

        self.snake_list[0].forward(20)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.snake_list[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.snake_list[0].setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.snake_list[0].setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.snake_list[0].setheading(RIGHT)

    def reset(self):
        for seg in self.snake_list:
            seg.goto(1000, 1000)
        self.snake_list.clear()
        self.setup_snake()
        self.head = self.snake_list[0]
        