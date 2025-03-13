from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.squares = []
        head_x_position = 0

        for _ in range(3): # Spawning the snake's whole body
            new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(head_x_position, 0)
            head_x_position -= 20
            self.squares.append(new_square)
        self.head = self.squares[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        for i in range(len(self.squares)-1, 0, -1): # The squares are following each other
            x = self.squares[i - 1].xcor()
            y = self.squares[i - 1].ycor()
            self.squares[i].goto(x, y)
        self.squares[0].forward(20) # The snake's "head" is moving forward by 20 paces at each update