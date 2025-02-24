from turtle import Turtle, Screen
import turtle as t
import random

turtle = Turtle()
screen = Screen()
t.colormode(255)

# challenge code 1
# create a square
# for i in range(0, 4):
#     turtle.forward(100)
#     turtle.right(90)

# challenge code 2
# draw a dotted line
# for i in range(0, 50):
#     turtle.forward(5)
#     turtle.penup()
#     turtle.forward(5)
#     turtle.pendown()

# challenge 3
# draw a shapes and color
colors = ['red', 'yellow', 'black', 'blue', 'green', 'brown', 'violet']
direction = [0,90, 180, 360]
# for i in range(4, 10):
#     angle = 360 / i
#     color = random.choice(colors)
#     turtle.color(color)
#     for j in range(0, i):
#         turtle.forward(100)
#         turtle.right(angle)
def rand_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# turtle.color
# turtle.pensize(10)
turtle.speed(20)
# for i in range(0, 100):

#     turtle.color(rand_color())
#     turtle.setheading(random.choice(direction))
#     turtle.forward(20)

for i in range(0, 50):
    turtle.color(rand_color())
    turtle.circle(100)
    turtle.right(10)

screen.exitonclick()