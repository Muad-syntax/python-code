import time
import turtle
from turtle import *

bg = Screen()
bg.bgcolor('black')

pen = turtle.Turtle()
pen.pencolor('pink')
pen.width(3)

def curva():
    for i in range(200):
        pen.rt(1)
        pen.fd(1)

def love():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.lt(140)
    pen.fd(113)
    curva()
    pen.lt(120)
    curva()
    pen.fd(112)
    pen.end_fill

love()
pen.ht()

def tulis(pesan, pos):
    x,y=pos
    pen.penup()
    pen.goto(x,y)
    pen.color('red')
    # style=('Stencil Std', 18, 'italic')
    pen.write(pesan, font=("Stencil", 18, "italic"), align="center")
tulis('I',(-68,95))
time.sleep(0.1)
tulis('L',(-55,95))
time.sleep(0.1)
tulis('O',(-42,95))
time.sleep(0.1)
tulis('V',(-29,95))
time.sleep(0.1)
tulis('E',(-14,95))
time.sleep(0.1)
tulis('Y',(10,95))
time.sleep(0.1)
tulis('O',(26,95))
time.sleep(0.1)
tulis('U',(45,95))
time.sleep(0.1)
tulis(' ',(-68,70))
time.sleep(5)