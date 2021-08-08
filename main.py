import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

loop_counter = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars_manage = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loop_counter += 1
    if loop_counter % 20 == 0:
        car = cars_manage.spawn_car()

    for car in cars_manage.cars:
        if player.distance(car) < 20:
            score.game_over()
            game_is_on = False

    if player.ycor() > 290:
        score.increase_score()
        player.start()
        cars_manage.level_up()


screen.exitonclick()