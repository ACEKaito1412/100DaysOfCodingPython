from turtle import Turtle
from bullet import Bullet

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(0.5, 1.5)
        self.penup()
        self.move_distance = 5
        self.go_to_start() 
        self.bullet_list = []
        self.lives = 3
        self.score = 0

    def update(self, ships):
        for bullet in self.bullet_list[:]:
            if bullet.ycor() > 200:
                bullet.hideturtle()
                self.bullet_list.remove(bullet)

            bullet.move_towards()
            if ships.check_collision(bullet):
                self.bullet_list.remove(bullet)
                self.score += 100


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
        bullet = Bullet(True, self.xcor() + 2, self.ycor())
        self.bullet_list.append(bullet)