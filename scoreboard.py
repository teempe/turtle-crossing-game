from turtle import Turtle


class Scoreboard(Turtle):
    """
    Class used to track player's score and show it on screen.

    Attributes
    ----------
    score : int
        current player's score

    Methods
    -------
    print_score()
        Prints actual player's score
    update_score()
        Increments player's score
    game_over()
        Prints game over when game is finished
    """

    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-220, 240)
        self.print_score()

    def print_score(self):
        """Prints actual player's score."""

        self.clear()
        self.write(f"Level: {self.score}", align="center", font=("Courier", 18, "bold"))

    def update_score(self):
        """Increments player's score."""

        self.score += 1
        self.print_score()

    def game_over(self):
        """Prints game over when game is finished."""

        self.goto(0, -20)
        self.write("GAME OVER", align="center", font=("Courier", 24, "bold"))
