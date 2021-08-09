
import random

lst=[random.randint(1,1000) for i in range(20)]

def lucky(L):
    return dothething(L, 0)


def dothething(L, num):
    if len(L)!=num:
        L[num]=7
        return dothething(L, num+1)
    else:
        return L

def dothething2(L):
    print("")

print(lucky(lst))

def lucky2(L):
    L[0]=7
    L2=L[::-1]
    num=L2.index(7)
    if num!=-1 and num!=0:
        L[len(L)-(num)]=7
        return lucky2(L)
    else:
        return L
    

print(lucky2(lst))
