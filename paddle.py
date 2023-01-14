from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(5,1)
        self.goto(x_pos,y_pos)

    def up(self):
        new_pos = self.ycor() + 15
        self.goto(self.xcor(), new_pos)

    def down(self):
        new_pos = self.ycor() - 15
        self.goto(self.xcor(), new_pos)