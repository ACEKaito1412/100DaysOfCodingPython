import time
import player
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

p = Player()
scoreboard = Scoreboard()
cars = CarManager()
screen.listen()
screen.onkey(p.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(cars.move_speed)
    screen.update()
    cars.move_cars()

    if p.ycor() == player.FINISH_LINE_Y:
        print("Finish")
        p.start()
        scoreboard.update_scoreboard()
        cars.increase_speed()

    if cars.is_hit(p):
        scoreboard.game_over()
        game_is_on = False
        


screen.exitonclick()