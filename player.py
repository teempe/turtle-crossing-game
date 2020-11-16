from turtle import Turtle


class Player(Turtle):
    """
    Class used to represent player.

    Methods
    -------
    move_up()
        moves player object forward
    set_start_position()
        sets player object to initial position
    """

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.set_start_position()

    def move_up(self):
        """Moves player object forward."""

        self.forward(10)

    def set_start_position(self):
        """Sets player object to initial position."""

        self.goto(0, -280)
