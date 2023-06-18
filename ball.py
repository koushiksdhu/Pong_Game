from turtle import Turtle       # Importing Turtle class from turtle module.
import time

class Ball(Turtle):         # Class Ball inheriting from the parent class Turtle.

    def __init__(self):         # Default constructor or Initialization.
        super().__init__()      # Calling the Data members and methods of the parent class using super method.
        self.shape("circle")    # Defining the shape of the turtle using shape method.
        self.color("#ffffff")   # Defining the color of the turtle using color method.
        self.penup()            # Penup.
        self.x_move = 10        # Variable containing the move value.
        self.y_move = 10        # Variable containing the move value.
        self.move_speed = 0.1

    def move(self):                             # Method move.
        new_x = self.xcor() + self.x_move       # Variable new _x containing the addition of current x coordinate value and the move value .
        new_y = self.ycor() + self.y_move       # variable new_y containing the addition  of current y coordinate value and the move value.
        self.goto(new_x, new_y)                 # Method goto is used to go to a particular position.
        time.sleep(self.move_speed)                         # sleep method.
        
    def y_bounce(self):                         # Method y_bounce.
        self.y_move *= -1                       # Setting the y coordinate value in the reverse/opposite direction.    
        self.move_speed *= 0.9
        
    def x_bounce(self):                         # Method x_bounce.
        self.x_move *= -1                      # Setting the x coordinate value in the reverse/opposite direction. 
        self.move_speed *= 0.9

    def reset_position(self):                   # Method reset_position.
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_bounce()


