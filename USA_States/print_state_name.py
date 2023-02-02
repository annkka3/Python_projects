from turtle import Turtle

class State(Turtle):
    def __init__(self, state_name, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(state_name)


