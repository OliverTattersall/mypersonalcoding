from turtle import *
import random
x=random.randint(20,500)

speed(1000)

for i in range(x):
    left(5)
    forward(100+i)
    left(90)
    forward(100+i)
    left(90)
    forward(100+i)
    left(90)
    forward(100+i)

print(x)
