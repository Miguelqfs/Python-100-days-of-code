from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 200)
        self.write(f"0  0", align="center", font=("Courier", 60, "normal"))

    def refresh(self, r_score, l_score):
        self.clear()
        self.write(f"{r_score}  {l_score}", align="center", font=("Courier", 60, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="center", font=("Courier", 70, "normal"))