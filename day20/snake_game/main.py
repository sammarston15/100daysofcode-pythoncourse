from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
snake_start_positions = [(0,0), (-20,0), (-40,0)]

snake_segments = []

for position in snake_start_positions:
    snake_segment = Turtle(shape='square')
    snake_segment.penup()
    snake_segment.color('white')
    snake_segment.goto(position)
    snake_segments.append(snake_segment)


game_is_on = True
while game_is_on:
    screen.update() 
    time.sleep(0.1)
    for seg_num in range(len(snake_segments) - 1, 0, -1):
        new_x = snake_segment[seg_num - 1].xcor()
        new_y = snake_segment[seg_num - 1].ycor()
        snake_segment[seg_num].goto(new_x, new_y)
    snake_segments[0].forwards(20)







screen.exitonclick()