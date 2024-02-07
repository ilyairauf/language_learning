import sqlite3
import tkinter



def connection():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    return c,conn


def get_words(is_new):
    c,conn = connection()
    c.execute("SELECT * FROM words")
    conn.commit()

    if is_new == True:
        return [row[0] for row in c.fetchall() if row[0] is not None]
    if is_new == False:
        return [row[2] for row in c.fetchall() if row[2] is not None]

def align_column_and_rows(window):
    for i in range(1, 20):
        window.columnconfigure(i, weight=1)

    for i in range(1, 20):
        window.rowconfigure(i, weight=1)

def destroy(is_set,is_delete,infobar,changing_word_entry,changing_word_submit,cancel_button):
    is_set,is_delete = False,False
    infobar.config(text='Welcome to your dictionary')
    if changing_word_entry.winfo_ismapped():
        changing_word_entry.grid_forget()
        changing_word_submit.grid_forget()
    cancel_button.grid_forget()
