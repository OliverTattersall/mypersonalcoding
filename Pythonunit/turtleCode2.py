from turtle import *
import random
speed(10000000)
colours=["red",'green', 'blue','yellow', 'orange', 'yellow','grey']
def square():
    for k in range(4):
        x=random.randint(0,5)
        color(colours[x])
        begin_fill()
        for i in range(4):
            forward(100)
            right(90)
        forward(100)
        pencolor(colours[x])
        end_fill()
    
for j in range(4):
    penup()
    goto(-200,j*100)
    pendown()
    square()

done()