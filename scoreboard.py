from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.shape("turtle")
        self.penup()
        self.goto(0, 260)
        self.write(arg=f"Level: {self.level}", align="center", font=FONT)
        self.hideturtle()

    def level_up(self):
        self.clear()
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", align="center", font=FONT)


