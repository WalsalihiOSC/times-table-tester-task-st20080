#Times Table Task
from tkinter import *
from tkinter import ttk
import random

class TimesTable:

    def __init__(self, parent):

        self.question = ttk.Label(parent, text = "") 
        self.question.grid(row = 0, column=0)

        self.input = ttk.Entry(parent, width = 10)

        self.check = ttk.Button(parent, text = "Check Answer")

        self.next = ttk.Button(parent, text = "Start")
        self.next.grid(row = 0, column = 1)

        self.feedback = ttk.Label(parent, text = "Click 'Start' to begin!")
        self.feedback.grid(row = 0, column = 0)
