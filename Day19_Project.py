# Day 19 project from 100 Days of Code: The Complete Python Pro Bootcamp course

from turtle import Turtle, Screen
import random as ra

is_race_on = False

color = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtles = []

screen = Screen()
screen.setup(500, 400)

for turtle_index in range(0, 6):
    race_turtle = Turtle(shape="turtle")
    race_turtle.penup()
    race_turtle.color(color[turtle_index])
    race_turtle.goto(x=-230, y=y_pos[turtle_index])
    all_turtles.append(race_turtle)


user_bet = screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ").lower()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner.")
            else:
                print(f"You lost! The {winning_color} turtle is the winner.")

        else:
            random_distance = ra.randint(0, 10)
            turtle.forward(random_distance)

screen.exitonclick()
