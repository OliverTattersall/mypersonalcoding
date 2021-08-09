import random
count=0
mylist=[]
def makelistfunction():
    for i in range(20):
        x=random.randint(1,1000)
        if x>105:
            mylist.append(x)
            mylist.sort()
            print(mylist)
makelistfunction()
