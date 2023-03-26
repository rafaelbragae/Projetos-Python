from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-210,260)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def car_crash(self):
        self.home()
        self.write("GAME OVER!", align="center", font=FONT)

