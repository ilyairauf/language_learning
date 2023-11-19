import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Program')

# Get screen dimensions
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set window size and position
window_width = 1000
window_height = 700
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

# Label
label = tk.Label(root, text='This is a label', font=('Helvetica', 30))
label.grid(row=2, column=0, columnspan=19, sticky='nsew', pady=(20, 0))

# Buttons with enhanced appearance
style = ttk.Style()
style.configure("TButton", font=('Helvetica', 14), padding=10)
button1 = ttk.Button(root, text='Practice')
button1.grid(row=4, rowspan=2, column=3, columnspan=3, sticky='nsew', padx=10, pady=10)

button2 = ttk.Button(root, text='Add new words')
button2.grid(row=7, rowspan=2, column=3, columnspan=3, sticky='nsew', padx=10, pady=10)

button3 = ttk.Button(root, text='Delete words')
button3.grid(row=10, rowspan=2, column=3, columnspan=3, sticky='nsew', padx=10, pady=10)

button4 = ttk.Button(root, text='Set words')
button4.grid(row=4, rowspan=2, column=13, columnspan=3, sticky='nsew', padx=10, pady=10)

button5 = ttk.Button(root, text='check out the words')
button5.grid(row=7, rowspan=2, column=13, columnspan=3, sticky='nsew', padx=10, pady=10)

button6 = ttk.Button(root, text='Settings')
button6.grid(row=10, rowspan=2, column=13, columnspan=3, sticky='nsew', padx=10, pady=10)

# Configure weights for columns and rows
for i in range(1, 19):
    root.columnconfigure(i, weight=1)

for i in range(1, 13):
    root.rowconfigure(i, weight=1)

root.mainloop()
