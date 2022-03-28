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
  random_color = (r, g, b)
  return random_color



# tim.pensize(10)

for i in range(150):
  tim.circle(100)
  tim.color(random_color())
  tim.left(10)

screen = Screen()
screen.exitonclick()