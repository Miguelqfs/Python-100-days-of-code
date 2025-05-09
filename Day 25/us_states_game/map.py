from turtle import Turtle

class MapNames(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        pass

    def add(self, x, y, state):
        self.goto(x=x, y=y)
        self.write(state)