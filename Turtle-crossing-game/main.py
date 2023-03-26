import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(player.up,"Up")

count = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move_car()
    if count == 6:
        car.create_car()
        count = -1
    end = player.finish()
    if end:
        score.level += 1
        car.up_level()
        score.update_score()
    count += 1
    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
score.car_crash()

screen.exitonclick()
