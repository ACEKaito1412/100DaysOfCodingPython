from turtle import Turtle
ALIGNMENT = "center"
FONTSTYLE = ("Arial", 18, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.level = 1
        self.hideturtle()
        self.start()

    def start(self):
        self.goto(0 , 170)
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level {self.level} | Score: {self.score}", align = ALIGNMENT, font=FONTSTYLE)

    def update_score(self, n):
        self.score += n
