import turtle as t
from turtle import Turtle, Screen
import random

tim = Turtle()
t.colormode(255)
tim.speed('fastest')


def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  color = (r, g, b)
  return color



# tim.pensize(10)
def draw_spirograph(size_of_gap):
  for i in range(int(360 / size_of_gap)):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(tim.heading() + size_of_gap)


draw_spirograph(5)

screen = Screen()
screen.exitonclick()