from turtle import Turtle
import random

WIDTH = 500
HEIGHT = 400


class Fodder(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh_position()

    def refresh_position(self):
        rand_x = random.uniform(-(WIDTH / 2 - 10), (WIDTH / 2 - 10))
        rand_y = random.uniform(-(HEIGHT / 2 - 10), (HEIGHT / 2 - 10))
        self.goto(x=rand_x, y=rand_y)

