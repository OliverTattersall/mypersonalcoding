import random

def binarysearch(l, item, issorted):
    if not issorted:
        l.sort()
    
    start = 0
    end = len(l)-1
    while end-start!=0:
        mid = (end+start)//2
        midval=l[mid]

        if midval==item:
            return mid
        if midval<item:
            start = midval+1
            # l = l[midval+1: ]
        else:
            end = midval-1
            #l = l[:midval]

    return None


l = [i for i in range(10)]

print(l)

print(binarysearch(l, 4, True))
print(binarysearch(l, 10, True))
print(binarysearch(l, 5, True))