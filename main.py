import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter.messagebox import showinfo as msg
from tkinter import messagebox as mb


conn = sqlite3.connect('database.db')
c = conn.cursor()

#c.execute(f"DELETE FROM words WHERE rowid = 6")
#conn.commit()


def Add():
    for widget in root.winfo_children():
       widget.destroy()
    
    for i in range(1, 20):
        root.columnconfigure(i, weight=1)

    for i in range(1, 20):
        root.rowconfigure(i, weight=1)
    
    button_exit  = ttk.Button(root, text='<-',command = main_window)
    button_exit.grid(row=1, column=2,  padx=1, pady=1)

    Entry = ttk.Entry(root, font=('Helvetica', 25),width=35)
    Entry.grid(row=2, column=2,columnspan = 10,)
    
    def Add_database():
        data = Entry.get()
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('SELECT * FROM words')
        conn.commit()
        words = [row[0] for row in c.fetchall()]
        if data and not data.isspace() and data not in words:
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute(f'INSERT INTO words (New_word,Number_of_iterations) VALUES(?,?)',(data,0))
            conn.commit()
            conn.close()
            msg = ttk.Label(root,text = 'Your word succesfully added!',font=('Helvetica', 15))
            msg.grid(row=3,column=3)
        elif data in words:
            mb.showwarning('word exist','this word already exists in your dictionary')
    button_submit  = ttk.Button(root, text='submit',command = Add_database)
    button_submit.grid(row=2, column=17,  padx=1, pady=1)
    def on_enter_key(event):
        button_submit.invoke()
    root.bind('<Return>',on_enter_key)

def check():

    def on_list_click():
        if mylist.curselection() != ():
            selected_item= mylist.get(mylist.curselection())
            ans = mb.askquestion('delete word',f"delete word','Are you sure you want to delete {selected_item}  ?")
            if ans == 'yes':
                mylist.delete(mylist.curselection())
                c.execute("DELETE FROM words WHERE New_word = ?", (selected_item,))
    
                conn.commit()

    for widget in root.winfo_children():
       widget.destroy()
 
    button_exit  = ttk.Button(root, text='<-----',command = main_window)
    button_exit.grid(row=1, column=2,  padx=1, pady=1,sticky='nsew')

    set_word = ttk.Button(root, text='Set words')
    set_word.grid(row=2, rowspan=2, column=2, padx=10, pady=10)

    delete_word = ttk.Button(root, text='Delete words',command=on_list_click)
    delete_word.grid(row=4, rowspan=2, column=1,  columnspan=3, padx=10, pady=10)

    for i in range(1, 20):
        root.columnconfigure(i, weight=1)

    for i in range(1, 20):
        root.rowconfigure(i, weight=1)
    
    scrollbar = ttk.Scrollbar(root)
    #scrollbar.grid(row = 1,column=10,sticky='nsew')
    scrollbar.grid(row=2, column=20, rowspan=19, sticky='nsew')

    mylist = tk.Listbox(root, yscrollcommand = scrollbar.set, selectbackground="#a6a6a6", selectforeground="black", exportselection=False, height=19, selectmode="single", bg="#f0f0f0", relief="flat", bd=0, font=('Helvetica', 15))

    c.execute('SELECT * FROM words')
    conn.commit()


    for line in c.fetchall():
        mylist.insert(0,line[0])

    
    mylist.grid(row=2, column=19, rowspan=19, sticky='nsew')
    scrollbar.config( command = mylist.yview )

    



def main_window():
    for widget in root.winfo_children():
        widget.destroy()


    # Label
    label = tk.Label(root, text='This is a label', font=('Helvetica', 30))
    label.grid(row=2, column=0, columnspan=19, sticky='nsew', pady=(20, 0))


    # Buttons with enhanced appearance
    style = ttk.Style()
    style.configure("TButton", font=('Helvetica', 14), padding=10)
    button1 = ttk.Button(root, text='Practice')
    button1.grid(row=4, rowspan=2, column=3, columnspan=3, sticky='nsew', padx=10, pady=10)

    button2 = ttk.Button(root, text='Add new words', command = Add)
    button2.grid(row=7, rowspan=2, column=3, columnspan=3, sticky='nsew', padx=10, pady=10)

    button5 = ttk.Button(root, text='check out the words',command = check)
    button5.grid(row=7, rowspan=2, column=13, columnspan=3, sticky='nsew', padx=10, pady=10)

    button6 = ttk.Button(root, text='Settings')
    button6.grid(row=4, rowspan=2, column=13, columnspan=3, sticky='nsew', padx=10, pady=10)

    # Configure weights for columns and rows
    for i in range(1, 19):
        root.columnconfigure(i, weight=1)

    for i in range(1, 13):
        root.rowconfigure(i, weight=1)

    root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    root.title('Program')

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    window_width = 1000
    window_height = 700
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    main_window()
    root.mainloop()
