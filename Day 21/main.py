# Hello! Welcome to the final version of the Snake Game Project!

# This is the main file, which controls all the features from other classes (one in each file).
# In this project, I learned a lot of Python OOP functionalities.
# I also created a lot of classes to make projects more scalable.

from time import sleep
from food import Food
from scoreboard import ScoreBoard
from screen import SetScreen
from snake import Snake

screen = SetScreen()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
score = 0

# Setting the snake's interactable movement mechanics
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect collision with food:
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score += 1
        scoreboard.update(score)

    # Detect collision with wall:
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail:
    for square in snake.squares[1:]: # Using list/tuple SLICING technique
        if snake.head.distance(square) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()