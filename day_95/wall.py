from turtle import Turtle
from bullet import Bullet

class Wall(Turtle):
    def __init__(self, x_pos:int, y_pos:int):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(0.1, 0.1)
        self.is_destroyed = False
        self.goto(x=x_pos,y=y_pos)

class Walls():
    def __init__(self):
        self.wall_list = []
        self.wall_size = 4
        self.wall_width = 10

    
    def create_walls(self):
        y_dir = -100
        for i in range(6):
            x_dir = -150
            if i % 2 == 0:
                for j in range(self.wall_size):
                    for k in range(self.wall_width):
                        x_dir += 5
                        wall = Wall(x_pos=x_dir, y_pos=y_dir)
                        self.wall_list.append(wall)
                    x_dir += 30
                    print(f"hello {x_dir}")
            y_dir -= 5

    
    def check_collision(self, bullet:Bullet):
        for wall in self.wall_list[:]:
            if wall.xcor() - 2 <= bullet.xcor() <= wall.xcor() + 2 and wall.ycor() - 1 <= bullet.ycor() <= wall.ycor() + 1:
                wall.is_destroyed = True
                wall.hideturtle()
                self.wall_list.remove(wall)
                return True
                
        return False