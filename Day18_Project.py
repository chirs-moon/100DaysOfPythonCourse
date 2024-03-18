# Day 18 project from 100 Days of Code: The Complete Python Pro Bootcamp course

import random as ra
import turtle as tu

rgb_colors = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40),
              (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148),
              (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171),
              (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100),
              (107, 127, 153), (174, 94, 97), (176, 192, 209)]

tu.colormode(255)
programming_turtle = tu.Turtle()
programming_turtle.penup()
programming_turtle.speed("fastest")
programming_turtle.setheading(225)
programming_turtle.forward(300)
programming_turtle.setheading(0)
programming_turtle.hideturtle()


for dot_count in range(1, 101):
    programming_turtle.dot(20, ra.choice(rgb_colors))
    programming_turtle.forward(50)
    if dot_count % 10 == 0:
        programming_turtle.setheading(90)
        programming_turtle.forward(50)
        programming_turtle.setheading(180)
        programming_turtle.forward(500)
        programming_turtle.setheading(0)

screen = tu.Screen()
screen.exitonclick()
