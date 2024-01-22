from turtle import Turtle

WIDTH = 500
HEIGHT = 400
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.goto(x=0, y=HEIGHT / 2 - 20)
        self.color("white")
        self.read_file()
        self.write(f"Your Score: {self.score} | High score {self.high_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.update_score()

    def read_file(self):
        with open(file="highest_score.txt", mode="r") as file:
            self.high_score = int(file.read())

    def add_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        with open(file="highest_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")
        self.write(f"Your Score: {self.score} | High score {self.high_score}", align=ALIGNMENT, font=FONT)
    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
