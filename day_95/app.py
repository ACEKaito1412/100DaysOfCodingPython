from turtle import * 
from player import Player
import time
from bullet import Bullet
from ships import Ships
from scoreboard import ScoreBoard
from wall import Walls

# Set up screen
screen = Screen()
screen.title("My Game")
screen.bgcolor("gray")
screen.setup(width=360, height=440)
screen.tracer(0)


# Title Text
title_turtle = Turtle()
title_turtle.hideturtle()
title_turtle.color("black")
title_turtle.penup()
title_turtle.goto(0, 100)

# Instructions
inst_turtle = Turtle()
inst_turtle.hideturtle()
inst_turtle.color("black")
inst_turtle.penup()
inst_turtle.goto(0, 40)

# Start Prompt
start_turtle = Turtle()
start_turtle.hideturtle()
start_turtle.color("yellow")
start_turtle.penup()
start_turtle.goto(0, -100)

# Function to clear the start screen
def start_game():
    title_turtle.clear()
    inst_turtle.clear()
    start_turtle.clear()
    screen.onkey(None, "Return")  # Disable key after pressing
    start_main_game()

def main_screen():
    title_turtle.write("🚀 Space Defender 🚀", align="center", font=("Arial", 24, "bold"))
    inst_turtle.write("Use arrow keys to move\nPress Space to shoot", align="center", font=("Arial", 16, "normal"))
    start_turtle.write("Press Enter to Start", align="center", font=("Arial", 18, "bold"))

    screen.listen()
    screen.onkey(start_game, "Return")

def start_main_game():
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
            scoreboard.clear()
            ships.clear()
            walls.clear()
            player.clear()
            player.hideturtle()
            main_screen()
            
        time.sleep(0.1)
        screen.update()
        player.update(ships, walls)
        ships.update(player, walls)

        scoreboard.update_scoreboard(player)

        if len(ships.ships) == 0:
            start_main_game()


main_screen()
screen.mainloop()