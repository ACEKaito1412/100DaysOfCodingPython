from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.create_cars()
        self.move_speed = STARTING_MOVE_DISTANCE * 0.05
    
    def create_cars(self):
        for i in range(0, 8):
            car_n = random.randint(8, 10)
            start_position = random.randint(250, 300)
            for j in range(2, car_n):
                n = random.randint(2, 3)
                x_position = (start_position - (j + 1) * 70) * n
                y_position = (300 - (i + 1) * 60)

                if x_position > -700:
                    car = Turtle()
                    car.penup()
                    car.shape("square")
                    car.shapesize(stretch_wid=1, stretch_len=1.5)
                    car.setpos(x= x_position,y = y_position )
                    car.color(random.choice(COLORS))
                    self.cars_list.append(car)

    def move_cars(self):
        for car in self.cars_list:
            new_x = car.xcor() - MOVE_INCREMENT
            car.goto(x = new_x, y = car.ycor())

            if car.xcor() < -700:
                car.setpos(x = 400, y = car.ycor())

    def increase_speed(self):
        self.move_speed *= 0.9

    def is_hit(self, player_turtle):
        for car in self.cars_list:
            if car.distance(player_turtle) < 15:
                return True
            
        return False