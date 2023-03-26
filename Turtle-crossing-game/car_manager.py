from turtle import Turtle
from scoreboard import Scoreboard
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5




class CarManager():

    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(1.5, 3)
        new_car.penup()
        new_car.color(random.choice(COLORS))
        starting_y = random.randint(-240, 250)
        new_car.setheading(180)
        new_car.goto(300, starting_y)
        self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.speed)

    def up_level(self):
        self.speed += MOVE_INCREMENT

