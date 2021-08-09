from tkinter import *

root=Tk()
root.geometry("300x300+0+0")

def sayhello():
    labe=Label(root, fg='red', text="Fuck you in the bum St. Mikes Style")
    labe.pack()
    

stop=Button(root,fg= 'red', text="Quit", command=quit)
stop.pack()
hello=Button(root, fg = 'deep sky blue', text="Hello", command=sayhello)
hello.pack()

mainloop()