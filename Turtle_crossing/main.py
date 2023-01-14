import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle = Player()
score = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(turtle.go_straight, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.car_move()

    # if the turtle collides with a car
    for car in cars.all_cars:
        if car.distance(turtle) < 20:
            game_is_on = False
            score.game_over()

    # if the turtle reach up safely
    if turtle.ycor() > 280:
        turtle.return_start()
        score.update_level()
        score.update_score()
        cars.increase_speed()





screen.exitonclick()