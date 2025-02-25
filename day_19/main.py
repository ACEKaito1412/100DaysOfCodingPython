import turtle as t
import random

is_game_on = False
screen = t.Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput("Make a bet.", "Which turtle will win the race: ")
colors = ["red","orange", "yellow", "green", "blue", "purple"]
turtles = []

for i in range(0, len(colors)):
    n = t.Turtle(shape="turtle")
    n.color(colors[i])
    n.penup()
    n.goto(-230, 150 - ((i + 1 ) * 40 ))
    turtles.append(n)

if user_bet:
    is_game_on = True

while is_game_on:
    for i in range(0, len(turtles)):
        turtle = turtles[i]
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        cur_pos = turtle.pos()
        if cur_pos[0] == 195:
            is_game_on = False
            bet_index = colors.index(user_bet.lower())

            if bet_index == i:
                print(f"You Win: The winner is {colors[i]}")
            else:
                print(f"You Lose: The winner is {colors[i]}")
            break
    

screen.exitonclick()