from turtle import *
from colorsys import *
tracer(30)
bgcolor("black")
h = 0
for i in range(2800):
    h+=0.0008
    color(hsv_to_rgb(h,1,1))
    if i % 5 == 0:
        right(3)
    forward(165)
    right(360/5)
    hideturtle()
done()