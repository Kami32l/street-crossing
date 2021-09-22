from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 1

screen = Screen()

# used to create custom shape turtle
# rectCors = ((-10, 20), (10, 20), (10, -20), (-10, -20))
# screen.register_shape('rectangle', rectCors)

starting_positions = \
    [
        (random.randint(300, 600), random.randrange(150, 180, 10)),
        (random.randint(300, 600), random.randrange(110, 140, 10)),
        (random.randint(300, 600), random.randrange(70, 100, 10)),
        (random.randint(300, 600), random.randrange(20, 60, 10)),
        (random.randint(300, 600), random.randrange(-60, -20, 10)),
        (random.randint(300, 600), random.randrange(-90, -70, 10)),
        (random.randint(300, 600), random.randrange(-130, -100, 10)),
        # (random.randint(300, 600), random.randint(-180, -155, 10)),

        (random.randint(600, 900), random.randrange(150, 180, 10)),
        (random.randint(600, 900), random.randrange(110, 140, 10)),
        (random.randint(600, 900), random.randrange(70, 100, 10)),
        (random.randint(600, 900), random.randrange(20, 60, 10)),
        (random.randint(600, 900), random.randrange(-60, -20, 10)),
        (random.randint(600, 900), random.randrange(-90, -70, 10)),
        (random.randint(600, 900), random.randrange(-130, -100, 10)),
        # (random.randint(600, 900), random.randint(-180, -155))
    ]


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.starting_positions = starting_positions
        self.move_distance = STARTING_MOVE_DISTANCE
        self.hideturtle()
        self.segments = []
        self.create_segments()

    def create_segments(self):
        for position in self.starting_positions:
            self.add_segment(position)
        screen.update()

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.shapesize(1, 2)
        new_segment.color(random.choice(COLORS))
        new_segment.penup()
        new_segment.goto(position)
        new_segment.seth(180)
        self.segments.append(new_segment)

    def move(self):
        for segment in self.segments:
            if segment.xcor() > -300:
                segment.forward(self.move_distance)
            else:
                index = self.segments.index(segment)
                segment.color(random.choice(COLORS))
                y_pos = self.starting_positions[index][1]
                x_pos = random.randrange(300, 450, 10)
                segment.goto(x_pos, y_pos)

    def next_level(self):
        self.move_distance += MOVE_INCREMENT
