from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.allCars = []

    def createCars(self):
        randomChance = random.randint(1, 6)
        if randomChance == 1:

            newCar = Turtle("square")
            newCar.shapesize(stretch_wid=1, stretch_len=2)
            newCar.penup()
            newCar.color(random.choice(COLORS))
            randomY = random.randint(-250, 250)
            newCar.goto(300, randomY)
            self.allCars.append(newCar)

    def moveCars(self):
        for car in self.allCars:
            car.backward(STARTING_MOVE_DISTANCE)