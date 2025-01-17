from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        # Left Player Score
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        # Right Player Score
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def left_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def winning(self):
        self.goto(0, 0)
        self.write("YOU WIN!", align=ALIGNMENT, font=FONT)
