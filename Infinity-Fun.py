from turtle import *
bgcolor('white')
color('red')
speed(15)
right(45)
for x in range(150):
    circle(30)
    if 7 < x < 62:
        left(5)
    if 80 < x < 133:
        right(5)
    if x < 80:
        forward(10)
    else:
        forward(5)