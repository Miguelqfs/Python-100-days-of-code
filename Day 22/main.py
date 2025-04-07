# Welcome to the Pong Game!
# This is a very famous game which I had so much fun making it.
# I hope you enjoy it and understand my code LOL :)
# To play it you should just run the main.py file.
# If you have any questions, you can just contact me through LinkedIn any time!
# My LinkedIn profile: www.linkedin.com/in/queirozmiguel

import time
from turtle import Screen
from ball import CreateBall
from paddle import CreatePaddle
from scoreboard import Scoreboard

# Setting the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# Creating objects
right_paddle = CreatePaddle((350, 0))
left_paddle = CreatePaddle((-350, 0))
ball = CreateBall((0,0))
score = Scoreboard()

# Adding paddle moving mechanics
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

# Verify if the ball touches the right paddle
def touched_right_paddle():
    if 350 <= ball.xcor() <= 360:
        if 0 <= ball.ycor() - right_paddle.ycor() <= 35 or 0 <= right_paddle.ycor() - ball.ycor() <= 35:
            return True
        else:
            return False
    return False

# Verify if the ball touches the left paddle
def touched_left_paddle():
    if -350 >= ball.xcor() >= -360:
        if 0 <= ball.ycor() - left_paddle.ycor() <= 35 or 0 <= left_paddle.ycor() - ball.ycor() <= 35:
            return True
        else:
            return False
    return False

x_pace = 10
y_pace = 10
r_player_points = 0
l_player_points = 0
game_speed = 0.1

game_is_on = 1
while game_is_on:
    time.sleep(game_speed)
    screen.update()
    ball.move(x_pace=x_pace, y_pace=y_pace)
    if ball.ycor() >= 290:
        y_pace = -10
    elif ball.ycor() <= -290:
        y_pace = 10
    elif touched_right_paddle():
        x_pace = -10
        game_speed -= 0.01
    elif touched_left_paddle():
        x_pace = 10
        game_speed -= 0.01
    elif ball.xcor() >= 400 or ball.xcor() <= -400:
        match ball.out_of_bounds():
            case 1:
                x_pace = -10
                r_player_points += 1
            case 2:
                x_pace = 10
                l_player_points += 1
        ball.goto(0, 0)
        score.refresh(l_score=l_player_points, r_score=r_player_points)
        game_speed = 0.1
        right_paddle.reset_paddle((350, 0))
        left_paddle.reset_paddle((-350, 0))

    if r_player_points == 3 or l_player_points == 3:
        score.game_over()
        game_is_on = False

screen.exitonclick()