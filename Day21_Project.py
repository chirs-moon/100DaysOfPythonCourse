# Day 21 project from 100 Days of Code: The Complete Python Pro Bootcamp course
import random
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


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.goto(random_x, random_y)
        self.refresh()

    def refresh(self):
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.goto(random_x, random_y)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def gameover(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()


scoreboard = Scoreboard()


def add_segment(position):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)


def extend():
    add_segment(segments[-1].position())


for position in starting_positions:
    add_segment(position)

food = Food()

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
    time.sleep(0.07)
    move_forward()

    if head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        extend()

    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        game_is_on = False
        scoreboard.gameover()

    for segment in segments[1:]:
        if head.distance(segment) < 10:
            game_is_on = False
            scoreboard.gameover()


screen.exitonclick()
