# README:

# Welcome to the turtle race project! This is the main one!
# I used OOP to get it done, and it was super fun to make this game. Hope you enjoy!

# Rules: type the color of which you think will win, and watch if you made a good bet. Good luck!

import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()

y_position = -100
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position)
    y_position += 30
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            if user_bet == turtle:
                print(f"You've won! The {turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle is the winner!")
        distance = random.randint(0,10)
        turtle.forward(distance)


screen.exitonclick()
