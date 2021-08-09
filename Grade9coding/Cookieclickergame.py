from tkinter import *
import time


def increasepoints():
    global pts
    global increaser
    pts = pts + increaser
    label.configure(text=pts)
    return pts

def increaserp():
    global pts
    global increaser
    global cost
    if pts>(cost-1):
        pts=pts-cost
        increaser=increaser+1
        #cost=int(((cost*cost)/25)+5)
        cost=int(cost*1.4)
        label.config(text=pts)
        inlabel.config(text=increaser)
        increaserb.config(text="pay " + str(cost)+" to upgrade your clicker")
        return pts
    else:
        notenough=Label(root, text="NOT ENOUGH POINTS")
        notenough.place(x=170,y=200)
def increaserp1():
    global pts
    global increaser
    global cost1
    if pts>(cost1-1):
        pts=pts-cost1
        increaser=increaser+6
        #cost=int(((cost*cost)/25)+5)
        cost1=int(cost1*1.3)
        label.config(text=pts)
        inlabel.config(text=increaser)
        increaserb1.config(text="pay " + str(cost1)+" to upgrade your clicker")
        return pts
    else:
        notenough=Label(root, text="NOT ENOUGH POINTS")
        notenough.place(x=170,y=200)

'''def superpoints():
    global pts
    pts=pts-100
    x=1
    while x>0:
        pts=pts + 10
        time.sleep(2)
        label.config(text=pts)'''




increaser=1
cost=25
cost1=1000
    

root=Tk()
root.title("Gang gang cookie clicker")
root.geometry("400x400+0+0")

pts = 0


label=Label(root,text=pts)
label.place(x=170,y=230)

label1=Label(root,text="This is how much ")
label1.place(x=10,y=250)
label2=Label(root,text="each click is worth")
label2.place(x=10,y=270)

inlabel=Label(root,text=increaser)
inlabel.place(x=10,y=290)

points=Button(root,text="click to get points",command=increasepoints)
points.place(x=160,y=250)

increaserb=Button(root,text="pay " + str(cost)+" to upgrade your clicker", command=increaserp)
increaserb.place(x=160,y=280)

increaserb1=Button(root,text="pay " + str(cost1)+" to upgrade your clicker", command=increaserp1)
increaserb1.place(x=160,y=330)

'''constant=Button(root,text="pay 100 to get 10 points every second", command=superpoints)
constant.place(x=160,y=350)'''

mainloop()