# Hello! Welcome to the final version of my Turtle Crossing Project!

# In this project, I learned a lot of Python OOP functionalities.
# I also created a lot of classes to make projects more scalable.

# This is the main file, which controls all the features from other classes (one in each file).
# You can run it and enjoy the game :)

# P.S: If you have any questions or suggestions about this code, feel free to reach out to me!

import random
import time
from os import times
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Setting the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Setting the objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Adding movement mechanics
screen.listen()
screen.onkey(player.move, "Up")

# The game starts here:
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Setting the randomness of the car generations
    # And also moving them at every screen refresh
    random_chance = random.randint(1,6)
    if random_chance == 1:
        car_manager.create_car()
    car_manager.move_cars()

    # Verifying if the turtle collided with one of the cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
        
    # Verifying if the turte got to the final line
    # Also restarting the turtle's position when this happens
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()