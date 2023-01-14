from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f'Score = {self.score}', align='center', font=('Arial', 14, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER! Your score is {self.score}', align='center', font=('Arial', 14, 'normal'))

    def add_score(self):
        self.score += 1
        self.update_score()


