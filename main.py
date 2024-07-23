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
    time.sleep(0.01)    # Add a small delay to prevent high CPU usage
    ball.move()    # Starts moving the ball when game starts

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
