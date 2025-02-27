from turtle import Turtle, Screen
import time
from snake import Snake
from Food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_state = True
while game_state:
    screen.update()
    time.sleep(0.1)

    snake.move()
    

    # detect distance
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # detect wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_state = False
        scoreboard.game_over()

    # detect collision tail
    # if head collided with a segment with tails
    for segment in snake.snake_list[1:]:
        if snake.head.distance(segment) < 10:
            game_state = False
            scoreboard.game_over()

screen.exitonclick()