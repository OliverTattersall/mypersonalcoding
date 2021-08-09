import random
x=random.randint(0,1000)
counter=0

while counter<10:
    y=input("guess an integer between 1 and 1000(i.e: 100): ")
    if y.isdigit():
        y=int(y)
        if y<x:
            print("too low")
            counter=counter + 1
        elif y>x:
            print("too high")
            counter=counter+1
        elif y==x:
            print("correct")
            print(counter)
            break
        if counter==10:
            print("sorry, you lose, too many guesses")
            break
        