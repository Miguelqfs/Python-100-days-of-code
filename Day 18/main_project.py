# This is the main project!
# Basically it is going to draw a hirst-style painting using turtle module

# import colorgram
#
# colors = colorgram.extract('image.jpg', 21)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r # r == [0]
#     g = color.rgb.g # g == [1]
#     b = color.rgb.b # b == [2]
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

rgb_values = [(236, 35, 108), (221, 231, 237), (145, 28, 66), (230, 237, 232), (239, 75, 35),
              (7, 148, 95), (220, 171, 45), (183, 158, 47), (45, 191, 232), (28, 127, 194),
              (254, 223, 0), (125, 192, 78), (85, 27, 91), (243, 218, 56), (178, 40, 98), (44, 170, 114),
              (211, 132, 166), (206, 57, 35), (239, 162, 193)]

from turtle import Turtle, Screen
import random

def left_curve():
    pencil.left(90)
    pencil.forward(50)
    pencil.left(90)

def right_curve():
    pencil.right(90)
    pencil.forward(50)
    pencil.right(90)

# Creating screen and pencil objects:
pencil = Turtle()
screen = Screen()
screen.colormode(255)

# Setting the pencil:
pencil.teleport(-230, -230)
pencil.penup()
pencil.speed("fastest")
pencil.hideturtle()

for x in range(10):
    for y in range(10):
        pencil.dot(20, random.choice(rgb_values))
        if y != 9:
            pencil.forward(50)
    if x % 2 == 0:
        left_curve()
    else:
        right_curve()

screen.exitonclick()