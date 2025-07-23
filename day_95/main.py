from turtle import * 
from player import Player
import time
from bullet import Bullet
from ships import Ships
from scoreboard import ScoreBoard



def shoot(player):
    bullet = Bullet(True)

screen = Screen()
screen.setup(width=360,height=440)
screen.tracer(0)


player = Player()
ships = Ships()
scoreboard = ScoreBoard(player)


screen.listen()
screen.onkey(player.right, "d")
screen.onkey(player.left, "a")
screen.onkey(player.shoot, "w")

bullet_list = []


game_state = True
while game_state:
    if player.lives == 0:
        game_state = False
        
    time.sleep(0.1)
    screen.update()
    player.update(ships)
    ships.update(player)

    scoreboard.update_scoreboard(player)



screen.tracer(1)
screen.exitonclick()