from turtle import Turtle

FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.goto(-280, 260)
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()
        self.write(f"Your level is : {self.level}", align="left", font=FONT)


    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"Your level is : {self.level}", align="left", font=FONT)

    def score_when_cross(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(-15, 0)
        self.write(f"GAME OVER", align="center", font=FONT)