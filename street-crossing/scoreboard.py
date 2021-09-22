from turtle import Turtle
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-100, 160)
        self.level = 1
        self.print_level()

    def add_level(self):
        self.level += 1
        self.pencolor("black")
        self.print_level()

    def print_level(self):
        self.clear()
        self.write(f"Level: {self.level}!", align="right", font=FONT)

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=("Arial", 40, "normal"))
        self.goto(0, -40)
        if self.level >= 10:
            self.write(f"Am0izing! you reached level: {self.level}", align="center", font=("Arial", 25, "normal"))
        elif self.level >= 5:
            self.write(f"Noice! you reached level: {self.level}", align="center", font=("Arial", 25, "normal"))
        else:
            self.write(f"You could do better! you reached level: {self.level}", align="center",
                       font=("Arial", 25, "normal"))
