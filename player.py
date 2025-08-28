from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        """
        Initializes the Player object with initial properties and starting position.
        """
        super().__init__()
        self.shape("turtle")
        self.shapesize(1.5, 1.5)
        self.penup()
        self.setheading(90)  # Pointing the turtle upwards
        self.goto(STARTING_POSITION)  # Starting position at the bottom of the screen

    def move_turtle(self):
        """
        Moves the turtle forward by MOVE_DISTANCE units.
        """
        self.forward(MOVE_DISTANCE)

    def got_to_start(self):
        """
        Resets the turtle's position to the starting position at the bottom of the screen.
        """
        self.goto(STARTING_POSITION)
