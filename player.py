from turtle import Turtle
from car_manager import CarManager

STARTING_POSITION = (0, -280)
HEADING = 90
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(HEADING)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reposition(self):
        if self.ycor() > 280:
            self.goto(STARTING_POSITION)


