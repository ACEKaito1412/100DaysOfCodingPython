from turtle import Turtle, register_shape
from bullet import Bullet
from wall import Walls


register_shape("images/spaceship.gif")


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("images/spaceship.gif")
        self.shapesize(0.5, 1.5)
        self.penup()
        self.move_distance = 5
        self.go_to_start() 
        self.bullet_list = []
        self.lives = 3
        self.score = 0

    def update(self, ships, walls:Walls):
        for bullet in self.bullet_list[:]:
            if bullet.ycor() > 200:
                bullet.hideturtle()
                self.bullet_list.remove(bullet)

            bullet.move_towards()
            if ships.check_collision(bullet):
                self.bullet_list.remove(bullet)
                bullet.hideturtle()
                self.score += 100

            if walls.check_collision(bullet):
                self.bullet_list.remove(bullet)
                bullet.hideturtle()


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
        bullet = Bullet(True, self.xcor() - 0.5, self.ycor())
        self.bullet_list.append(bullet)