import numpy as np

x = np.arange(40).reshape(2,4,5)
length = 1
for i in x.shape:
    length*=i

sumt = sum(x)
while type(sumt)==np.ndarray:
    sumt=sum(sumt)
    




def findmax(array, foo):
    if type(array[0])!=np.ndarray:
        return foo(array)
    
    maxlist = []
    for i in array:
        maxlist.append(findmax(i, foo))
    return foo(maxlist)

print("Mean: ",sumt/length)
print("Max:", findmax(x, max))
print("Min:", findmax(x, min))



def convert(bool):
    if bool:
        return 1
    return 0

print(sum(map(convert, [True, True,False, False])))