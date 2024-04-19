from turtle import Turtle, Screen
from playsound import playsound
from scoreboard import Scoreboard
import time
import snake
import fodder

I = 0

WIDTH = 500
HEIGHT = 400
score = I
my_screen = Screen()
my_screen.bgcolor("black")
my_screen.title("My first game")
my_screen.title(f"Score board: {score}")
my_screen.setup(width=WIDTH, height=HEIGHT)
my_screen.tracer(I)
turtle_list = []
starting_position = [(I, I), (-20, I), (-40, I)]

snake = snake.Snake()
food = fodder.Fodder()
scoreboard = Scoreboard()
my_screen.update()

# for position in starting_position:
#     my_turtle = Turtle(shape="square", visible=True)
#     my_turtle.penup()
#     my_turtle.color("white")
#     my_turtle.goto(position)
#     turtle_list.append(my_turtle)
#
# # my_screen.update()
#

my_screen.listen()
my_screen.onkey(key="Up", fun=snake.up)
my_screen.onkey(key="Down", fun=snake.down)
my_screen.onkey(key="Left", fun=snake.left)
my_screen.onkey(key="Right", fun=snake.right)

game_is_on = True
while game_is_on:
    if 20 < score <= 40:
        time.sleep(0.05)
    elif score > 40:
        time.sleep(0.03)
    else:
        time.sleep(0.07)
    if snake.head.distance(food) < 12:
        score += 1
        scoreboard.increase_score()
        # my_screen.title(f"Your score: {score}")
        food.refresh_position()
        snake.extend_snake()
    my_screen.update()
    snake.snake()
    if snake.head.xcor() > (
            WIDTH / 2 - 1) or snake.head.ycor() > (HEIGHT/2 - 7) or snake.head.ycor() < -(HEIGHT/2 - 1) or snake.head.xcor() < -(WIDTH/2):
        # playsound("mixkit-arcade-fast-game-over-233.wav")
        scoreboard.add_high_score()
        snake.reset()
        # game_is_on = False
    for segment in snake.turtle_list[1:]:
        if snake.head.distance(segment) < 9.5:
            # game_is_on = False
            scoreboard.add_high_score()
my_screen.exitonclick()

