import turtle as t
import random

screen = t.Screen()
screen.setup(600, 500)
user_guess = screen.textinput(title="Turtle Bet Racing", prompt="Choose your turtle color from (red, blue, green, orange, yellow, purple): ")
is_race_on = False
color_list = ["red", "blue", "green", "orange", "yellow", "purple"]
xpath = [-100, -50, 0, 50, 100, 150]
timmy_group = []

for timmy in range(6):
    color = color_list[timmy]
    path = xpath[timmy]
    timmy = t.Turtle(shape="turtle")
    timmy.penup()
    timmy.color(color)
    timmy.goto(-250, path)
    timmy_group.append(timmy)

if user_guess:
    is_race_on = True

while(is_race_on):
    for race in timmy_group:
        if race.xcor() > 280:
            is_race_on = False
            if user_guess == race.pencolor():
                next_game = screen.textinput(title="You Won!", prompt=f"The {race.pencolor()} turtle wins! Did you enjoy?")
            else:
                next_game = screen.textinput(title="You Lose!", prompt=f"The {race.pencolor()} turtle wins! Did you enjoy?")
        speed_meter = random.randint(0, 10)
        race.forward(speed_meter)

screen.exitonclick()