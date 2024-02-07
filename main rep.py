import tkinter as tk
from tkinter import ttk
import sqlite3
import utilities
from main_window import Main

#c,conn = utilities.connection()
#c.execute('DELETE FROM words')
#conn.commit()
root = tk.Tk()
root.title('Program')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 1200
window_height = 700

x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2 -35

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
Main.main_window(root)

root.mainloop()