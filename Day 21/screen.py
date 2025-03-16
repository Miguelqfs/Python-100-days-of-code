from turtle import Screen

# This class sets the main settings of the screen.
class SetScreen(Screen):
    def __init__(self):
        super().__init__()
        self.setup(width=600, height=600)
        self.bgcolor("black")
        self.title("My snake game")
        self.tracer(0)