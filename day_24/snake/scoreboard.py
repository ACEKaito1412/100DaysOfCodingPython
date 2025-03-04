from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(x = 0, y=260)
        self.high_score = 0
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.update_scoreboard()
        self.read_score()
    
    def update_scoreboard(self):
        self.clear()
        self.write( f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('score.txt', 'w') as f:
                f.write(str(self.score))

        self.score = 0
        self.update_scoreboard()

    def read_score(self):
        with open('score.txt', 'r') as f:
            content = f.read()
            self.high_score  = int(content)
            return


    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
        

    def game_over(self):
        self.goto(0,0)
        self.write( f"GAME OVER", align=ALIGNMENT, font=FONT)