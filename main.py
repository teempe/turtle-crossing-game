"""Turtle Crossing Game.

Player must get through busy road (5 lanes each direction) unharmed. Every time he/she manages to get to the other side
speed of cars increases.
"""

from turtle import Screen
from time import sleep
from random import randint
from utils import draw_lanes
from player import Player
from car import Car
from scoreboard import Scoreboard


window = Screen()
window.setup(width=600, height=600)
window.colormode(255)
window.bgcolor("grey")
window.tracer(0)
draw_lanes()

player = Player()
level = Scoreboard()

window.listen()
window.onkey(key="Up", fun=player.move_up)

game_speed = 0.1
cars = []
counter = 0
is_game_on = True
while is_game_on:
    sleep(game_speed)
    window.update()

    # Create new car every 8th loop cycle (start in first cycle when counter=0)
    if counter == 0 or counter == 8:
        # Generate car in top lanes (rides from right to left)
        lane_number = randint(1, 5)                     # Choose lane number
        cars.append(Car(180, (300, lane_number * 40)))  # Create car at top lane heading West

        # Generate car in bottom lanes (rides from left to right)
        lane_number = randint(1, 5)                     # Choose lane number
        cars.append(Car(0, (-300, lane_number * -40)))  # Create car at bottom lane heading East

        counter = 0                                     # reset counter

    for car in cars:
        car.move()

        # If car gets outside window remove it from list
        if car.xcor() < -340 or car.xcor() > 340:
            cars.remove(car)

        # Collision with car (player's coordinates +/-20 from car center)
        if (car.xcor() - 20 <= player.xcor() <= car.xcor() + 20) \
                and (car.ycor() - 20 <= player.ycor() <= car.ycor() + 20):
            is_game_on = False
            level.game_over()

    # Check if player gets to the other side of the road
    if player.ycor() > 280:
        game_speed *= 0.9           # Speed up game at next level
        player.set_start_position()
        level.update_score()

    counter += 1

window.exitonclick()
