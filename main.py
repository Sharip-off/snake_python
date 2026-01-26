from turtle import Turtle, Screen
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []


for position in starting_position:
    t1 = Turtle(shape="square")
    t1.color("white")
    t1.penup()
    t1.goto(position)
    segments.append(t1)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)


screen.exitonclick()
