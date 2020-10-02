import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from tkinter.ttk import Treeview
from Data.dataBase import DataBase



class AddContactWindow(object):

    def __init__(self, root):
        self.root=root
        self.root = tk.Tk()
        self.root.title("Add Contact")
        self.root.geometry("400x400")
        self.root.resizable(False, False)
        self.wrapper3 = LabelFrame(self.root, text="Add New")
        self.wrapper3.pack(fill="both", expand="yes", padx=20, pady=10)

        self.label1 = Label(self.wrapper3, text="First Name:")
        self.label1.grid(column=1, row=1, padx=5, pady=3)
        self.entry1 = Entry(self.wrapper3)
        self.entry1.grid(column=2, row=1, padx=7, pady=3)

        self.label2 = Label(self.wrapper3, text="Last Name:")
        self.label2.grid(column=1, row=2, padx=5, pady=3)
        self.entry2 = Entry(self.wrapper3)
        self.entry2.grid(column=2, row=2, padx=7, pady=3)

        self.label3 = Label(self.wrapper3, text="Email:")
        self.label3.grid(column=1, row=3, padx=5, pady=3)
        self.entry3 = Entry(self.wrapper3)
        self.entry3.grid(column=2, row=3, padx=7, pady=3)

        self.label4 = Label(self.wrapper3, text="Phone #:")
        self.label4.grid(column=1, row=4, padx=5, pady=3, )
        self.entry4 = Entry(self.wrapper3)
        self.entry4.grid(column=2, row=4, padx=7, pady=3)

        self.button = Button(self.wrapper3, text="Submit")
        self.button.grid(column=2, row=5, padx=5, pady=3)

        self.root.mainloop()

    dataBase = DataBase()






