from turtle import * 
from player import Player
import time
from bullet import Bullet
from ships import Ships



def shoot(player):
    bullet = Bullet(True)

screen = Screen()
screen.setup(width=360,height=400)
screen.tracer(0)


player = Player()
ships = Ships()

screen.listen()
screen.onkey(player.right, "d")
screen.onkey(player.left, "a")
screen.onkey(player.shoot, "w")

bullet_list = []


game_state = True
while game_state:
    time.sleep(0.1)
    screen.update()
    player.update(ships)
    ships.update()



screen.tracer(1)
screen.exitonclick()