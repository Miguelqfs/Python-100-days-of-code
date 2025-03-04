import random
import turtle
from turtle import Turtle, Screen
# from turtle import * -> You can import everything inside turtle's module (*). Not too convenient
# import turtle as t -> You can rename the module name.

timmy_the_turtle = Turtle()
screen = Screen()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("slateblue2") # Colour chosen from https://cs111.wellesley.edu/reference/colors

turtle.colormode(255)
# function that creates an RGB tuple to use as a parameter for the method .pencolor
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    r_color = (r, g, b)

    return r_color

timmy_the_turtle.pensize(15)
timmy_the_turtle.speed("fastest")
angles = [0,90,180,270]

for _ in range(200):
    timmy_the_turtle.pencolor(random_color())
    timmy_the_turtle.forward(30)
    timmy_the_turtle.right(random.choice(angles))

screen.exitonclick()