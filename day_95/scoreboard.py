from turtle import Turtle
from player import Player
ALIGNMENT = "center"
FONTSTYLE = ("Arial", 13, "normal")

class ScoreBoard(Turtle):
    def __init__(self, player:Player):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0 , 190)
        self.update_scoreboard(player)
    
    def update_scoreboard(self, player:Player):
        self.clear()
        self.write(f"Lives {player.lives} | Score: {player.score}", align = ALIGNMENT, font=FONTSTYLE)

    def update_score(self, n):
        self.score += n
