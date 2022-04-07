#Times Table Task
global total
y=0  
from tkinter import *
from tkinter import ttk
n= ttk.Notebook()
f1= ttk.Frame(n)
f2= ttk.Frame(n)

window= ttk.Frame(n)

def main(x):
    global total,user_input,entry
    n.add(f1, text="Question One")
    n.add(f2, text="Question Two")

    total= ttk.Label(window, text="0")
    user_input = StringVar
 
main(y)

n.pack()

n.mainloop()
