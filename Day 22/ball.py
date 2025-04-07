from turtle import Turtle

class CreateBall(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("slowest")
        self.goto(position)
        self.color("white")

    def move(self, x_pace, y_pace):
        self.goto(self.xcor() + x_pace, self.ycor() + y_pace)

    def out_of_bounds(self):
        if self.xcor() >= 400:
            return 1
        elif self.xcor() <= -400:
            return 2