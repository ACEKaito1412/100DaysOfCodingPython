# from turtle import Turtle, Screen

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color('red')  

# timmy.forward(100)


# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["picachu", "charmander", "squirtle"])
table.add_column("Field Type", ["elictric", "fire", "water"])
table.align = "l"

print(table)
