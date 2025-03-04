import random
import turtle
from turtle import Turtle, Screen
# from turtle import * -> You can import everything inside turtle's module (*). Not too convenient
# import turtle as t -> You can rename the module name.

timmy_the_turtle = Turtle()
screen = Screen()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("slateblue2") # Colour chosen from https://cs111.wellesley.edu/reference/colors

timmy_the_turtle.speed("fastest")
turtle.colormode(255)

# function that creates an RGB tuple to use as a parameter for the method .pencolor
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb_color = (r, g, b)

    return rgb_color

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy_the_turtle.pencolor(random_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + size_of_gap)

draw_spirograph(5)

screen.exitonclick()