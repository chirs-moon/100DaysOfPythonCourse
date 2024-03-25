# Day 25 project from 100 Days of Code: The Complete Python Pro Bootcamp course

# import csv
import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)

# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#     print(temperatures)

# Creates DataFrame
# data = pandas.read_csv("weather_data.csv")
# print(data)

# Creates Series
# temperature_list = data["temp"].to_list()
# print(round(sum(temperature_list) / len(temperature_list), 2))
#
# print(data["temp"].max())
# print(data.temp.max())

# Prints a row where the value in the day column is equal to "Monday"
# print(data[data.day == "Monday"])

# Prints a row where the value in the temp column is the highest
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp = monday_temp * 9 / 5 + 32
# print(monday_temp)

# Creating a DataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)

# data = pandas.read_csv("central_park.csv")
# grey_sq = len(data[data["Primary Fur Color"] == "Gray"])
# black_sq = len(data[data["Primary Fur Color"] == "Black"])
# red_sq = len(data[data["Primary Fur Color"] == "Cinnamon"])
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [grey_sq, red_sq, black_sq]
# }
#
# data_sq = pandas.DataFrame(data_dict)
# data_sq.to_csv("sq_count.csv")


# def get_mouse_click_cor(x, y):
#     print(x, y)


screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
# turtle.onscreenclick(get_mouse_click_cor)
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_date = data[data.state == answer_state]
        t.goto(int(state_date.x), int(state_date.y))
        t.write(state_date.state.item())

screen.exitonclick()
