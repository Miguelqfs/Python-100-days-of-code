from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]

# This class initializes the snake and adds its functionality
class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    # Creates snake in the starting position:
    def create_snake(self):
        for position in STARTING_POSITIONS: # Spawning the snake's whole body
            self.add_segment(position)

    # When it's called, adds one more segment(square) to the snake:
    def add_segment(self, position):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.squares.append(new_square)

    # Extends the snake by one tail segment:
    def extend(self):
        self.add_segment(self.squares[-1].position())

    # Moving mechanics:
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

    # More moving mechanics:
    def move(self):
        for i in range(len(self.squares)-1, 0, -1): # The squares are following each other
            x = self.squares[i - 1].xcor()
            y = self.squares[i - 1].ycor()
            self.squares[i].goto(x, y)
        self.squares[0].forward(20) # The snake's "head" is moving forward by 20 paces at each update