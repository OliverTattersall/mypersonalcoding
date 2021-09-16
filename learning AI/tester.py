import numpy as np 
import random

sizes = [1, 4, 2, 5, 6]

x=[np.random.randn(y,1) for y in sizes[1:]]
print(x)
print(x[0], x[1])


print(list(zip((1,2,3), (4,5,6))))
for x, y in zip(sizes[:-1], sizes[1:]):
    print(x,y)