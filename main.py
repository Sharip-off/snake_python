from turtle import Turtle, Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")

starting_position = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_position:
    t1 = Turtle(shape="square")
    t1.color("white")
    t1.goto(position)

screen.exitonclick()