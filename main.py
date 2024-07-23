from turtle import Screen
from ball import Ball
from paddle import RightPaddle, LeftPaddle
import time

# Set up Screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)    # Turn off animations temporarily

# Set up Paddles
right_paddle = RightPaddle()
left_paddle = LeftPaddle()

# Player Paddle Controls
left_paddle.controls(screen)

# Set up ball
ball = Ball()

# Main Game Loop
is_game_on = True

while is_game_on:
    screen.update()     # Turn on animations again after paddles are initialized in their proper positions
    time.sleep(0.01)    # Add a small delay
    ball.move()         # Starts moving the ball when game starts

    # Bounce ball when making contact with top or bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with right or left paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 330 or ball.distance(left_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 390:
        ball.reset_position()

    # Detect when left paddle misses
    if ball.xcor() < -390:
        ball.reset_position()