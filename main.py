import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            player.go_to_start()
            scoreboard.game_over()
            game_is_on = False

    #detect if player reach the top of the screen
    if player.if_at_finish_line():
        player.go_to_start()
        scoreboard.score_when_cross()
        car_manager.increase_speed_car()

screen.exitonclick()


# move the turtle with key press

#create and move the traffic

#detect collision with car_manager

#detect when turtle eraches the other side

# create a scoreboard
