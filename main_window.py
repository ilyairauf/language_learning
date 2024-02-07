import tkinter as tk
from tkinter import ttk
import sqlite3
import utilities
from practise import Practise
from add import Add
from check import Check

class Main:

    def main_window(root):
        for widget in root.winfo_children():
            widget.destroy()

        label = tk.Label(root, text='Language learning', font=('Helvetica', 30))
        label.grid(row=2, column=0, columnspan=19, sticky='nsew', pady=(20, 0))

        style = ttk.Style()
        style.configure("TButton", font=('Helvetica', 14), padding=10)

        button1 = ttk.Button(root, text='Practice',command=lambda: Practise.practice(root,Main.main_window))
        button1.grid(row=4, rowspan=2, column=3, columnspan=3, sticky='nsew', padx=10, pady=10)

        button2 = ttk.Button(root, text='Add new words', command = lambda: Add.add(root,Main.main_window))
        button2.grid(row=7, rowspan=2, column=3, columnspan=3, sticky='nsew', padx=10, pady=10)

        button5 = ttk.Button(root, text='Settings')
        button5.grid(row=7, rowspan=2, column=13, columnspan=3, sticky='nsew', padx=10, pady=10)

        button6 = ttk.Button(root, text='check out the words',command = lambda: Check.check(root,Main.main_window))
        button6.grid(row=4, rowspan=2, column=13, columnspan=3, sticky='nsew', padx=10, pady=10)

        # Configure weights for columns and rows
        for i in range(1, 19):
            root.columnconfigure(i, weight=1)

        for i in range(1, 13):
            root.rowconfigure(i, weight=1)

        root.mainloop()

    def __init__(self):
        pass