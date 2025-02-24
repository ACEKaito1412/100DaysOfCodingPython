import turtle as t
import random as r
import colorgram

colors = colorgram.extract("OIP.jpg", 6)

turtle = t.Turtle()
screen = t.Screen()
t.colormode(255)
turtle.pensize(20)
turtle.color('red')

def rand_color():
    c = r.choice(colors)
    return c.rgb
turtle.penup()
turtle.setposition(-200, -200)
turtle.pendown()
for i in range(0, 10):
    for j in range(0, 10):
        turtle.color(rand_color())
        turtle.forward(1)
        turtle.penup()

        if j < 9:
            turtle.forward(50)
            turtle.pendown()
    
    if i < 9:
        turtle.penup()
        pos = turtle.pos()
        turtle.setpos(-200, pos[1] + 50)
        turtle.pendown()
screen.exitonclick()