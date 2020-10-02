from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as Tk
from PIL import Image, ImageTk
from tkinter.ttk import Treeview
from Data.dataBase import DataBase
from Views.addContact import AddContactWindow
import sqlite3 as sql

class AboutUsWindow(object):
    def __init__(self, root):
        self.root = root
        self.root = Tk.Tk()
        self.root.title("About Us")
        self.root.geometry("280x400")

        # Team Jp3 logo
        self.photo = Tk.PhotoImage(master=self.root, file="C:\\Users\\jhali\\PycharmProjects\\Phone-Book\\Images\\about_us.png")

        self.photo_label = Tk.Label(self.root, image=self.photo)
        self.photo_label.grid(row=0, column=0, padx=10, pady=10)

        # Application information
        self.label = Tk.Label(master=self.root, text="Address-Book by Team Jp3\n Version 1.0\n Copyright © 2020")
        self.label.grid(row=2, column=0, padx=10, pady=10)

        self.root.mainloop()