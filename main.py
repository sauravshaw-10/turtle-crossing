import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)
screen.listen()

player = Player()
cars = CarManager()
level = Scoreboard()

screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.make_cars()
    cars.move()

    # Increasing car speed and levels
    if player.ycor() > 280:
        cars.increment_speed()
        level.level_up()
        player.reposition()

    # Detect collision with cars
    for car in cars.all_cars:
        if player.distance(car) < 21:
            game_is_on = False
            level.game_over()


screen.exitonclick()
