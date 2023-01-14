from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('SNAKE GAME')
screen.tracer(0)

segments =[]

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.extend()
    #detect collision with wall
    if not (-290 < snake.head.xcor() < 290) or not ( -290 < snake.head.ycor() < 290):
        score.game_over()
        game_is_on = False
    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 1:
            score.game_over()
            game_is_on = False











screen.exitonclick()