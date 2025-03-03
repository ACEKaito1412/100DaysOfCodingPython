
from turtle import Turtle
ALIGNMENT = "center"
FONTSTYLE = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.player_1 = 0
        self.player_2 = 0
        self.start()
    
    def start(self):
        self.goto(0, 160)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.player_1} \t : \t {self.player_2}", align=ALIGNMENT, font=FONTSTYLE)

    def update_player_1(self):
        self.player_1 +=1
        self.update_scoreboard()
    
    def update_player_2(self):
        self.player_2 +=1
        self.update_scoreboard()
     
    def show_winner(self):
        self.clear()
        self.goto(0, 0)
        if self.player_1 > self.player_2:
            self.write(f"WINNER IS PLAYER 1", align=ALIGNMENT, font=FONTSTYLE)
        elif self.player_1 < self.player_2:
            self.write(f"WINNER IS PLAYER 2", align=ALIGNMENT, font=FONTSTYLE)