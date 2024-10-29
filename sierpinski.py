# lab06b_fractal.py
# This program draws a Sierpinski fractal figure
from turtle import *
import random

def sierpinski(length, depth):
    if depth == 1:
        colormode(255)
        r = int(random.random() * 255)
        g = int(random.random() * 255)
        b = int(random.random() * 255)
        color(r,g,b)
    if depth > 1: dot()  # mark position to better see recursion
    if depth == 0:  # base case
        stamp()  # stamp a triangular shape
    else:
        forward(length)
        sierpinski(length / 2, depth - 1)  # recursive call
        backward(length)
        left(120)
        forward(length)
        sierpinski(length / 2, depth - 1)  # recursive call
        backward(length)
        left(120)
        forward(length)
        sierpinski(length/2,depth - 1) # recursive call
        backward(length)
        left(120)

        # create a drawing screen
ts = getscreen()
ts.title("Colorful Sierpinski Fractal")
speed(0)
sierpinski(200, 6)
hideturtle()
ts.exitonclick()

