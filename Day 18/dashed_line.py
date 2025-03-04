from turtle import Turtle, Screen
# from turtle import * -> You can import everything inside turtle's module (*). Not too convenient
# import turtle as t -> You can rename the module name.

timmy_the_turtle = Turtle()
screen = Screen()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("slateblue2") # Colour chosen from https://cs111.wellesley.edu/reference/colors

# Drawing dashed line:
for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()

screen.exitonclick()