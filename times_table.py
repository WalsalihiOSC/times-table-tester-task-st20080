#Times Table Task
from tkinter import *
from tkinter import ttk
import random

class TimesTable:

    def __init__(self, parent):

        self.question = ttk.Label(parent, text = "") 
        self.question.grid(row = 0, column=0)

        self.input = ttk.Entry(parent, width = 10)

        self.check = ttk.Button(parent, text = "Check Answer", command = self.Check)

        self.next = ttk.Button(parent, text = "Start", command = self.Next)
        self.next.grid(row = 0, column = 1)

        self.feedback = ttk.Label(parent, text = "Click 'Start' to begin!")
        self.feedback.grid(row = 0, column = 0)


    def Next(self):
        self.feedback.configure(text = "",)
        self.feedback.grid(row=1)
        self.question.configure(text = "Question: ") 
        num1 = random.randrange(1,10)
        num2 = random.randrange(1,10)
        display_question = "Question: {} {} {} = ".format(num1, "*", num2)
        self.answer = num1*num2
        self.question.configure(text = display_question)
        self.check.grid(row = 1, column = 1)
        self.input.grid(row = 0, column = 1)
        self.next.grid_remove()

    def Check(self):
        try:
            if int(self.input.get()) == int(self.answer):
                self.input.delete(0,END)
                self.input.focus()
                self.Next()
                self.feedback.config(text = "Correct")
            else:
                self.input.delete(0,END)
                self.input.focus()
                self.Next()
                self.feedback.config(text = "Incorrect")

        except ValueError:
            self.feedback.configure(text = "Incorrect Input")
            self.input.delete(0,END)
            self.input.focus()

if __name__ == "__main__":
    root = Tk()
    root.title("Times Table")
    TimesTable(root)
    root.mainloop()
