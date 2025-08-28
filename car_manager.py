import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        """
        Creates a new car and adds it to the list of all cars.

        Randomly creates a car with a certain probability.
        """
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.y_coordinate = random.randint(-250, 280)
            new_car.goto(280, new_car.y_coordinate)
            self.all_cars.append(new_car)

    def move_cars(self):
        """
        Moves all cars to the left by the current car_speed.
        """
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        """
        Increases the speed of cars when the player reaches the top of the screen.
        """
        self.car_speed += MOVE_INCREMENT
