# Day 20 project from 100 Days of Code: The Complete Python Pro Bootcamp course
import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

head = segments[0]


def up():
    if head.heading() != DOWN:
        head.setheading(UP)


def down():
    if head.heading() != UP:
        head.setheading(DOWN)


def left():
    if head.heading() != RIGHT:
        head.setheading(LEFT)


def right():
    if head.heading() != LEFT:
        head.setheading(RIGHT)


screen.update()
screen.listen()
screen.onkey(up, "w")
screen.onkey(down, "s")
screen.onkey(left, "a")
screen.onkey(right, "d")


def move_forward():
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    move_forward()

screen.exitonclick()
