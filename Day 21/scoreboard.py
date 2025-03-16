from turtle import Turtle

# This class was made to create and control de scoreboard and its functionality.
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.update(0)

    def update(self, score):
        self.clear()
        self.write(f"Score: {score}", False, align="center", font=('Courier', 20, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", False, align="center", font=('Courier', 30, 'normal'))
