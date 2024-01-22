import turtle
from turtle import Turtle

STARTING_POSITION = [(0, 0), (-10, 0), (-20, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]
        self.up_one = False
        self.down_one = False
        self.right_one = False
        self.left_one = False

    def create_snake(self):
        for position in STARTING_POSITION:
            if position == (0, 0):
                my_turtle = Turtle(shape="turtle", visible=True)
                my_turtle.penup()
                my_turtle.color("red")
                my_turtle.shapesize(stretch_wid=0.5, stretch_len=0.5)
                my_turtle.goto(position)
                self.turtle_list.append(my_turtle)
            self.add_segment(position)

    def add_segment(self, position):
        my_turtle = Turtle(shape="square", visible=True)
        my_turtle.penup()
        my_turtle.color("green")
        my_turtle.shapesize(stretch_wid=0.5, stretch_len=0.5)
        my_turtle.goto(position)
        self.turtle_list.append(my_turtle)

    def extend_snake(self):
        self.add_segment(self.turtle_list[-1].position())

    def snake(self):
        for seg_num in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[seg_num - 1].xcor()
            new_y = self.turtle_list[seg_num - 1].ycor()
            self.turtle_list[seg_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)

    def increase_snake_length(self):
        my_turtle = Turtle(shape="square", visible=True)
        my_turtle.penup()
        my_turtle.color("white")
        my_turtle.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.turtle_list.append(my_turtle)

    def reset(self):
        for seg in self.turtle_list:
            seg.goto(1000, 1000)
        self.turtle_list.clear()
        self.create_snake()
        self.head = self.turtle_list[0]
