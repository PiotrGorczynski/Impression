from turtle import *
from random import choice, randrange, randint

def polygon(x, y, n, length):
    penup()
    goto(x,y)
    pendown()
    pensize(2)
    color("black",choice(["red","green","white","orange","yellow","pink","blue"]))
    begin_fill()
    for i in range (n):
          forward(length)
          left(360/n)
    end_fill()

speed(0)
bgcolor("gray")
title("IMPRESSION")
for i in range(50):
    x=randint(-250,250)
    y=randint(-250,250)
    n=randint(3,12)
    dl=randint(5,32)
    polygon(x, y, n, dl)
hideturtle()
mainloop()
