from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.increase_score()
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)
        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)
        
    def write_game_over(self):
        self.goto(-100, 0)
        self.write("GAME OVER", font=("Courier", 30, "normal"))
        