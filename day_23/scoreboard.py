from turtle import Turtle
FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("black")
        self.level = 0
        self.goto(-230, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        game_text = Turtle()
        game_text.hideturtle()
        game_text.penup()
        game_text.color("black")
        game_text.goto(0, 0)
        game_text.write(f"Game Over !!", align=ALIGNMENT, font=FONT)