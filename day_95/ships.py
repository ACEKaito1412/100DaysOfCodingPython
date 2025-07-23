from turtle import Turtle
from bullet import Bullet
import random



class Ship(Turtle):
    def __init__(self, x_pos:int, y_pos:int):
        super().__init__()
        self.shape("square")
        self.shapesize(0.5, 1)
        self.penup()
        self.is_broken = False
        self.goto(x =x_pos, y=y_pos)
        self.curr_add = 0
        self.move_direction = True
        self.move_speed = 0.5
        self.switch = 0

    def update(self):
        if self.curr_add == 20:
            self.switch += 1
            self.move_direction = False
        elif self.curr_add == -20:
            self.move_direction = True

        if self.move_direction:
            self.curr_add += 1
            new_x = self.xcor() + self.move_speed
        else:
            self.curr_add -= 1
            new_x = self.xcor() - self.move_speed

        if self.switch == 3:
            self.switch = 0
            new_y = self.ycor() - 20
            self.goto(x = new_x , y = new_y)
        else:
            self.goto(x = new_x , y = self.ycor())




class Ships():
    def __init__(self):
        self.ships = {}
        self.layer = 3
        self.create_ships()
        self.bullets = []

    def create_ships(self):
        # 180 , 140
        n_y = 180
    
        for i in range(self.layer):
            n_x = -158
            array = []
            for j in range(10):
                n_x += 28
                ship = Ship(x_pos= n_x, y_pos=n_y)
                array.append(ship)
            n_y -= 20
            self.ships[i] = array

    def update(self):
        for i in range(self.layer):
            if len(self.bullets) < 3:
                print('hello')
                ship_ = random.choice(self.ships[i])

                if ship_:
                    self.shoot(ship_)

            for ship in self.ships[i]:
                if not ship.is_broken:
                    ship.update()

        for bullet in self.bullets[:]:
            bullet.move_towards()
            if bullet.ycor() < -200:
                self.bullets.remove(bullet)


    def check_collision(self, bullet)->bool:
        for key, value in self.ships.items():
            for item in value[:]:
                if item.is_broken == False:
                    if item.xcor() - 10 <= bullet.xcor() <= item.xcor() + 10 and item.ycor() - 2 <= bullet.ycor() <= item.ycor() + 2:
                        item.is_broken = True
                        item.hideturtle()
                        bullet.hideturtle()
                        value.remove(item)
                        return True
                    
        return False

    def shoot(self, ship:Ship):
        bullet = Bullet(False, x_pos= ship.xcor(), y_pos=ship.ycor())

        self.bullets.append(bullet)



