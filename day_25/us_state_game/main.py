import turtle
import pandas
from scoreboard import Scoreboard

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")
states = pandas.read_csv('50_states.csv')
names = states['state'].to_list()

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

score = Scoreboard()

answer_state = ""

def show_on_screen(answer, x , y):
    n_turtle = turtle.Turtle()
    n_turtle.penup()
    n_turtle.color('black')
    n_turtle.hideturtle()
    n_turtle.goto(x,y)
    n_turtle.write( f"{answer}", align=ALIGNMENT, font=FONT)

def save_to_csv(d):
    n_list = states[~states['state'].isin(d)].state
    
    n_data = {
        "state" : n_list
    }

    new_df = pandas.DataFrame(n_data)
    new_df.to_csv('miss_states.csv')

    

game_state = True
list_answer = []

while game_state:
    answer_state = screen.textinput("Guess the state", "What's another state name?").title()

    if answer_state == "Exit":
        save_to_csv(list_answer)
        break
    elif answer_state in names:
        list_answer.append(answer_state)
        loc_data = states[states.state == answer_state.title()]
        show_on_screen(answer_state.title(), float(loc_data.x), float(loc_data.y))
        score.increase_score()

    if score == 50 :
        game_state = False
