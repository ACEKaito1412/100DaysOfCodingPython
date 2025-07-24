from turtle import * 
from player import Player
import time
from bullet import Bullet
from ships import Ships
from scoreboard import ScoreBoard
from wall import Walls


screen = Screen()
screen.setup(width=360,height=440)
screen.tracer(0)


player = Player()
ships = Ships()
scoreboard = ScoreBoard(player)
walls = Walls()

walls.create_walls()

screen.listen()
screen.onkey(player.right, "d")
screen.onkey(player.left, "a")
screen.onkey(player.shoot, "w")



game_state = True
while game_state:
    if player.lives == 0:
        game_state = False
        
    time.sleep(0.1)
    screen.update()
    player.update(ships, walls)
    ships.update(player, walls)

    scoreboard.update_scoreboard(player)

    if len(ships.ships) == 0:
        pass



screen.tracer(1)
screen.exitonclick()