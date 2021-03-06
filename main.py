import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.goUp, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    carManager.createCars()
    carManager.moveCars()
    for car in carManager.allCars:
        if car.distance(player) < 20:
            scoreboard.gameOver()
            game_is_on = False

    if player.isAtFinishLine():
        player.goToStart()
        carManager.levelUp()
        scoreboard.increaseLevel()

screen.exitonclick()