from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.higher = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}    Higher Score: {self.higher}", False, align="center", font=("Arial", 24, "normal"))

    def add_score(self):
        self.score += 1
        self.update_score()

    def reset(self):
        if self.score > self.higher:
            self.higher = self.score
            with open("data.txt","w") as data:
                data.write(str(self.higher))

        self.score = 0
        self.update_score()

    # def end_game(self):
    #     self.clear()
    #     self.penup()
    #     self.home()
    #     self.write(f"GAME OVER! Your score was: {self.score}", False, align="center", font=("Arial", 20, "normal"))
