from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 20
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def spawn_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.goto(270, random.randint(-200, 200))
        new_car.setheading(180)
        self.cars.append(new_car)
        self.move()

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def move(self):
        for car in self.cars:
            car.forward(self.car_speed)
