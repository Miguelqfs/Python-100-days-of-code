from turtle import Turtle, Screen
# from turtle import * -> You can import everything inside turtle's module (*). Not too convenient
# import turtle as t -> You can rename the module name.

timmy_the_turtle = Turtle()
screen = Screen()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("slateblue2") # Colour chosen from https://cs111.wellesley.edu/reference/colors

# Drawing a square:
for _ in range(4):
    timmy_the_turtle.right(90) # In PyCharm, you can press 'F2' to rename something
    timmy_the_turtle.forward(100)

screen.exitonclick()