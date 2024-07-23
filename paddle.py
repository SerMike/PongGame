from turtle import Turtle

RIGHT_POSITION = (350, 0)
LEFT_POSITION = (-350, 0)
SCREEN_HEIGHT = 600
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()

class RightPaddle(Paddle):
    def __init__(self):
        super().__init__()
        self.teleport(RIGHT_POSITION[0], RIGHT_POSITION[1])

class LeftPaddle(Paddle):
    def __init__(self):
        super().__init__()
        self.teleport(LEFT_POSITION[0], LEFT_POSITION[1])

    def move_up(self):
        if self.ycor() < (SCREEN_HEIGHT / 2) - 50:
            new_y = self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -(SCREEN_HEIGHT / 2) + 50:
            new_y = self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def controls(self, screen):
        screen.listen()
        screen.onkeypress(self.move_up, "w")
        screen.onkeypress(self.move_down, "s")
