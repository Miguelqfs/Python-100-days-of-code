# README:

# In this project, I tested interactions with the keyboard. This is a very cool feature, and it is
# opening up my mind for new future projects!

from turtle import Turtle, Screen

screen = Screen()
tim = Turtle()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def look_right():
    tim.right(15)

def look_left():
    tim.left(15)

def clear_screen():
    tim.home()
    tim.clear()

screen.listen()

screen.onkey(move_forwards, "w") # Don't trigger the function, just pass it as a parameter
screen.onkey(move_backwards, "s")
screen.onkey(look_right, "d")
screen.onkey(look_left, "a")
screen.onkey(clear_screen, "c")

screen.exitonclick()
