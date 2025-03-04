import random
import turtle
import matplotlib.colors as mcolors
from turtle import Turtle, Screen
# from turtle import * -> You can import everything inside turtle's module (*). Not too convenient
# import turtle as t -> You can rename the module name.

timmy_the_turtle = Turtle()
screen = Screen()
timmy_the_turtle.shape("turtle")

for sides in range(3,11):
    angle = 360 / sides

    # Get a random colour from a color name list from matplotlib's module.
    mpl_colors = list(mcolors.CSS4_COLORS.keys())
    timmy_the_turtle.pencolor(random.choice(mpl_colors))

    for y in range(sides):
        timmy_the_turtle.right(angle)
        timmy_the_turtle.forward(100)

screen.exitonclick()