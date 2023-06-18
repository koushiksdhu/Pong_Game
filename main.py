from turtle import Screen           # Importing Screen class from the turtle module.
from paddle import Paddle           # Importing Paddle class from the paddle.py
from ball import Ball               # Importing Ball class from the ball.py       
from scoreboard import Scoreboard   # Importing Scoreboard class from the scoreboard.py

screen = Screen()                                   # Storing the Screen() method in screen variable.
screen.setup(width = 800, height = 600)             # Setting up the screen size of thw game window.
screen.bgcolor("#000000")                           # Setting up the background color of the screen to black(Hexcode: #000000).
screen.title("Pong Game - Made by Koushik Sadhu")   # Setting up the title of the screen.
screen.tracer(0)

right_paddle = Paddle((380, 0))         # Passing position of x and y in the form of tuple.
left_paddle = Paddle((-380, 0))         # Passing position of x and y in the form of tuple.
ball = Ball()
score = Scoreboard()

screen.listen()                         
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    
    # Detect collision with the wall:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
        
    # Detect collision with the right paddle and left paddle:
    if ball.distance(right_paddle) < 50 and ball.xcor() > 350 or ball.distance(left_paddle) < 50 and ball.xcor() < -350:
        ball.x_bounce()
        
    # Detect right paddle misses:
    if ball.xcor() > 390:
        score.update_left_score()
        ball.reset_position()
             
    # Detect left paddle misses:
    if ball.xcor() < -390:
        score.update_right_score()
        ball.reset_position()

screen.exitonclick()

# Note: If you're using a method as a parameter, then it should be not passed with parentheses. Only the name of the method should be passed.
