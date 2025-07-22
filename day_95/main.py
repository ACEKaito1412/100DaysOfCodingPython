from turtle import * 
from player import Player



screen = Screen()
screen.setup(width=300,height=400)
screen.tracer(0)


player = Player()


screen.listen()
screen.onkey(player.right, "d")
screen.onkey(player.left, "a")
screen.onkey(player.shoot, "w")




screen.tracer(1)
screen.exitonclick()