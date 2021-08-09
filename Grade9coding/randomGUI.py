from tkinter import *

def listmake():
    lst=""
    lst.append(entry.get())

root=Tk()
root.geometry("800x400+0+0")
root.title("fuck you")

label=Label(root,text="fuck you in the bum")
label.pack()

entry=Entry(root,command=listmake)
entry.pack()



mainloop()