#!/usr/bin/python3

# -------------- A program to make spiral graphics with turtle python3 ------------------

import turtle
import random

colors = ["red", "cyan", "pink", "yellow", "green", "orange"]
t = turtle.Turtle()
t.speed(10)
turtle.bgcolor("black")
length = 100
angle = 50
size = 5

for i in range(length):
    color = random.choice(colors)
    t.pencolor(color)
    t.fillcolor(color)
    t.penup()
    t.forward(i + 50)
    t.pendown()
    t.left(angle)
    t.begin_fill()
    t.circle(size)
    t.end_fill()

turtle.exitonclick()
