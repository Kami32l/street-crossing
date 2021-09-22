from turtle import Turtle

STARTING_POSITION = (0, -180)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()

    def set_up(self):
        self.go_to_starting_position()
        self.shape("square")
        self.seth(90)

    def go_to_starting_position(self):
        self.hideturtle()
        self.penup()
        self.goto(STARTING_POSITION)
        self.showturtle()

    def move(self):
        self.forward(MOVE_DISTANCE)
