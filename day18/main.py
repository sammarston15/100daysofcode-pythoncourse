import turtle as t
from turtle import Turtle, Screen
import random

tim = Turtle()
t.colormode(255)

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  random_color = (r, g, b)
  return random_color

directions = [0, 90, 180, 270]

tim.pensize(10)

for i in range(150):
  tim.forward(20)
  tim.color(random_color())
  tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()