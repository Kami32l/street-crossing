import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()


def game():
    screen.setup(width=600, height=400)
    screen.tracer(0)
    player = Player()
    player.set_up()
    scoreboard = Scoreboard()
    car_manager = CarManager()

    game_is_on = True
    while game_is_on:

        time.sleep(0.1)

        screen.listen()
        screen.onkey(player.move, "Up")

        # player.distance()
        if player.ycor() > 180:
            scoreboard.add_level()
            player.go_to_starting_position()
            car_manager.next_level()

        car_manager.move()
        screen.update()

        for segment in car_manager.segments:
            if player.distance(segment) < 20:
                game_is_on = False
                scoreboard.game_over()

    play_again = screen.textinput("Play again?", "Do you want to play again?").lower()

    if play_again != "no":
        screen.clear()
        game()


game()
