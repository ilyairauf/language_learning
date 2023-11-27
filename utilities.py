import sqlite3

conn = sqlite3.connect('database.db')
c = conn.cursor()

def get_words(is_new):
    c.execute("SELECT * FROM words")
    conn.commit()
    if is_new == True:
        return [row[0] for row in c.fetchall()]
    if is_new == False:
        return [row[2] for row in c.fetchall()]

def align_column_and_rows(window):
    for i in range(1, 20):
        window.columnconfigure(i, weight=1)

    for i in range(1, 20):
        window.rowconfigure(i, weight=1)



