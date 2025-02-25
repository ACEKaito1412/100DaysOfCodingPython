import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forward():
    tim.forward(10)

def move_backward():
    tim.forward(-10)

def rotote_right():
    tim.right(5)

def rotote_left():
    tim.left(5)

def clear_screen():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()

screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="d", fun=rotote_right)
screen.onkeypress(key="a", fun=rotote_left)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()