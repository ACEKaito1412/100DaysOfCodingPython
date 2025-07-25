from turtle import Turtle, register_shape
from bullet import Bullet
import random
from player import Player
from wall import Walls


register_shape("images/allien-1.gif")
register_shape("images/allien-2.gif")
register_shape("images/allien-3.gif")

class Ship(Turtle):
    def __init__(self, x_pos:int, y_pos:int, shape:str):
        super().__init__()
        self.shape(shape)
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
            shape = f"images/allien-{i+1}.gif"
            for j in range(10):
                n_x += 28
                ship = Ship(x_pos= n_x, y_pos=n_y, shape=shape)
                array.append(ship)
            n_y -= 20
            self.ships[i] = array

    def clear(self):
        for key, value in self.ships.items():
            for item in value[:]:
                item.hideturtle()
                value.remove(item)

        for bullet in self.bullets[:]:
            bullet.hideturtle()
            self.bullets.remove(bullet)


    def update(self, player:Player, walls:Walls):
        for i in range(self.layer):
            if len(self.bullets) < 3:
                ship_ = random.choice(self.ships[i])

                if not ship_.is_broken:
                    self.shoot(ship_)

            for ship in self.ships[i]:
                if not ship.is_broken:
                    ship.update()

                    if ship.ycor() > 200:
                        player.lives = 0
                    

        for bullet in self.bullets[:]:
            bullet.move_towards()

            if bullet.ycor() < -200:
                bullet.hideturtle()
                self.bullets.remove(bullet)

            if (player.xcor() - 10 <= bullet.xcor() <= player.xcor() + 10) and (bullet.ycor() <= -195):
                player.lives -= 1
                bullet.hideturtle()
                self.bullets.remove(bullet)
                print(player.lives)
            
            if walls.check_collision(bullet):
                bullet.hideturtle()
                self.bullets.remove(bullet)

    def check_collision(self, bullet:Bullet)->bool:
        for key, value in self.ships.items():
            for item in value[:]:
                if item.is_broken == False:
                    if item.xcor() - 10 <= bullet.xcor() <= item.xcor() + 10 and item.ycor() - 2 <= bullet.ycor() <= item.ycor() + 2:
                        item.is_broken = True
                        item.hideturtle()
                        value.remove(item)
                        bullet.hideturtle()
                        return True
                    
        return False

    def shoot(self, ship:Ship):
        bullet = Bullet(False, x_pos= ship.xcor(), y_pos=ship.ycor())

        self.bullets.append(bullet)