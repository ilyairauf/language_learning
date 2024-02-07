import tkinter as tk
from tkinter import ttk
import sqlite3
import utilities
import vocab



class Add:
    

    def add(root,callback):
        global c,conn
        c,conn = utilities.connection()

        for widget in root.winfo_children():
            widget.destroy()

            utilities.align_column_and_rows(root)
    
            button_exit  = ttk.Button(root, text='<-',command =lambda: callback(root))
            button_exit.grid(row=1, column=2,  padx=1, pady=1)

            Entry = ttk.Entry(root, font=('Helvetica', 25),width=25)
            Entry.grid(row=4, column=5,columnspan = 7,)

            translation_entry = ttk.Entry(root,font=('Helvetica', 25),width=25)
            translation_entry.grid(row=6,column=5,columnspan=7)

            word = tk.Label(root,text='word',font=('Helvetica',25))
            word.grid(row=4,column=4)

            word_translation_label = tk.Label(root,text='Translation',font=('Helvetica',25))
            word_translation_label.grid(row=6,column=4)

            infobar_Add = tk.Label(root,text=(''))
            infobar_Add.grid(row=7,column=5)
    
            def Add_database():
                word_entry_value = Entry.get()
                word_translation_value = translation_entry.get()
                c.execute('SELECT New_word, Translation_of_the_word, Learnt_word FROM words')
                conn.commit()
                words = c.fetchall()
                print(words)
                if word_entry_value !='' and  word_entry_value != '' and word_translation_value !=''  and word_entry_value not in words and len(word_entry_value)<27 and len(word_translation_value) <=27:

                    c.execute(f'INSERT INTO words (New_word,Number_of_iterations,translation_of_the_word,deleted) VALUES(?,?,?,?)',(word_entry_value,0,word_translation_value,0))
                    conn.commit()

                    infobar_Add.config(text = 'Your word succesfully added!',font=('Helvetica', 15),fg='green')
                    infobar_Add.grid(row=7,column=7)
                    Entry.delete('0','end')
                    translation_entry.delete('0','end')

                elif word_entry_value in words:
                    infobar_Add.config(text=("This word already exists in your dictionary"),fg='red',font=(10))
                    infobar_Add.grid(row = 7,column=7)
                elif len(word_entry_value) >=27 or len(word_translation_value) >=27:
                    infobar_Add.config(text=("Your word can't be longer than 27 letters"),fg='red',font=(10))
                    infobar_Add.grid(row = 7,column=7)
                elif  word_entry_value == '' or word_translation_value == '' :
                    infobar_Add.config(text=('Please fill in all required fields'),fg='red',font=(10))
                    infobar_Add.grid(row = 7,column=7)

            button_submit  = ttk.Button(root, text='submit',command = Add_database)
            button_submit.grid(row=4, column=17,rowspan=3,  padx=1, pady=1)

            def on_enter_key(event):
                button_submit.invoke()
            root.bind('<Return>',on_enter_key)
