from turtle import Turtle
from random import randint


class Car(Turtle):
    """
    Represents car as squared turtle 40 width and 20 height.

    Methods
    -------
    move()
        Moves the car 10 spaces forward
    """

    def __init__(self, head, start_pos):
        """
        Parameters
        ----------
        head : int or float
            Direction of the car in degrees
        start_pos : pair of numbers
            Coordinates of new car object
        """

        super().__init__()
        self.penup()
        self.shape("square")
        self.setheading(head)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(randint(0, 255), randint(0, 255), randint(0, 255))
        self.goto(start_pos)

    def move(self):
        """Moves car 10 spaces forward."""

        self.forward(10)
