from turtle import Turtle   # Importing Turtle class from turtle module.

class Paddle(Turtle):
    
    def __init__(self, position):       # Position is a tuple containing x and y coordinates.
        super().__init__()
        self.shape("square")
        self.color("#ffffff")
        self.penup()
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.goto(position)
          
    def go_up(self):            # Method always have an attribute as self.
        if self.ycor() < 240:
            self.new_y_coordinates = self.ycor() + 20
        self.goto(self.xcor(), self.new_y_coordinates)
        
    def go_down(self):          # Method always have an attribute as self.
        if self.ycor() > -240:
            self.new_y_coordinates = self.ycor() - 20
        self.goto(self.xcor(), self.new_y_coordinates)
