from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x = 0, y=260)
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.write( f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        

    def game_over(self):
        self.goto(0,0)
        self.write( f"GAME OVER", align=ALIGNMENT, font=FONT)