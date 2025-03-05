from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x = 0, y=250)
        self.high_score = 0
        self.color("black")
        self.score = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write( f"Score: {self.score} / 50", align=ALIGNMENT, font=FONT)

    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        