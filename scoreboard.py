from turtle import Turtle

FONT = ("TimesRoman", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        """
        Initializes the Scoreboard object with initial properties.
        """
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(-220, 260)  # Positioning the scoreboard
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Updates the scoreboard display with the current score.
        """
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        """
        Displays "GAME OVER!!!" message at the center of the screen.
        """
        self.goto(0, 0)  # Positioning the "GAME OVER!!!" message
        self.write(f"GAME OVER!!!", align="center", font=FONT)

    def increase_score(self):
        """
        Increases the score by 1 and updates the scoreboard display.
        """
        self.score += 1
        self.clear()  # Clears previous score display
        self.update_scoreboard()  # Updates the scoreboard with the new score
