from turtle import Turtle

# CONSTANTS:
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("#ffffff")
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.goto(200, 270)
        self.write(f"\tScore: {self.right_score}", align = "right", font = FONT)
        self.goto(-200, 270)
        self.write(f"Score: {self.left_score}", align = "left", font = FONT)
        
    def update_right_score(self):
        self.right_score += 1
        self.clear()
        self.goto(200, 270)
        self.write(f"\tScore: {self.right_score}", align = "right", font = FONT)
        self.goto(-200, 270)
        self.write(f"Score: {self.left_score}", align = "left", font = FONT)

    def update_left_score(self):
        self.left_score += 1
        self.clear()
        self.goto(200, 270)
        self.write(f"\tScore: {self.right_score}", align = "right", font = FONT)
        self.goto(-200, 270)
        self.write(f"Score: {self.left_score}", align = "left", font = FONT)

        