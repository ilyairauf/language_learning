import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter.messagebox import showinfo as msg
from tkinter import messagebox as mb
import time
import random
import utilities

#add button adjusted adjust set and delete  buttons

conn = sqlite3.connect('database.db')
c = conn.cursor()

#c.execute("""CREATE TABLE words(
#
#        New_word text,
#        Number_of_iterations integer,
#        Learnt_word text,
#        translation_of_the_word text
#    )
# """)
#conn.commit()
c.execute('SELECT * FROM words')
conn.commit()
print(c.fetchall())


def Add():
    for widget in root.winfo_children():
       widget.destroy()
    
    utilities.align_column_and_rows(root)
    
    
    button_exit  = ttk.Button(root, text='<-',command = main_window)
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
        words = utilities.get_words(True)
        
        if word_entry_value !='' and  word_entry_value != ''and word_translation_value !=''  and word_entry_value not in words and len(word_entry_value)<27 and len(word_translation_value) <=27:
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute(f'INSERT INTO words (New_word,Number_of_iterations,translation_of_the_word) VALUES(?,?,?)',(word_entry_value,0,word_translation_value))
            conn.commit()
            conn.close()
            
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

def check():

    def update_word():
        if mylist.curselection() == ():
            mb.showwarning('choose a word','You have to choose a word from list first')
        else:
            selected_index = mylist.curselection()
            updated_word = changing_word_entry.get()
            words = utilities.get_words(True) + utilities.get_words(False)
            if updated_word != '' and updated_word not in words:
                word_to_update = mylist.get(selected_index)
                c.execute("UPDATE words SET New_word = ? WHERE New_word = ?", (updated_word, word_to_update))
                c.execute("UPDATE words SET Learnt_word = ? WHERE Learnt_word = ?", (updated_word, word_to_update))
                c.execute("UPDATE words SET Translation_of_the_word = ? WHERE Translation_of_the_word = ?", (updated_word, word_to_update))
                
                conn.commit()
                mylist.delete(selected_index)
                mylist.insert(selected_index,updated_word)
                changing_word_entry.grid_forget()
                changing_word_submit.grid_forget()
                infobar.config(text="Welcome to your dictionary")
                global cancel_button,is_set
                cancel_button.grid_forget()
                is_set = False
            elif updated_word in words:
                mb.showerror('word already exist', "Sorry you can't update a word to an existing one")





    for widget in root.winfo_children():
       widget.destroy()  
    
    button_frame = tk.Frame(root,width=200,height=550,padx=15)#,borderwidth=2,relief='solid')
    button_frame.grid(row=2, column=2,  padx=1, pady=1)
    button_frame.grid_propagate(0)

    set_widgets_frame = tk.Frame(root,width=470,height=600)#,borderwidth=2,relief='solid')
    set_widgets_frame.grid(row = 1,columnspan=5,column=4,rowspan=2)
    set_widgets_frame.grid_propagate(0)

    global is_delete,is_set,is_learnt,is_translated,cancel_button,changing_word_entry,changing_word_submit
    is_delete,is_set,is_learnt,is_translated= False,False,False,True

      
    infobar = ttk.Label(set_widgets_frame, text='Welcome to your dictionary',font = ('Helvetica', 20))
    infobar.grid(row = 0, column = 8,columnspan=3)

    def translate():
        global is_translated,is_learnt
        is_translated = not is_translated
        mylist.delete(0,tk.END)
        c.execute('SELECT * FROM words')
        conn.commit()
        if is_learnt == False:
            if is_translated == False:
                for i in c.fetchall():
                    if i[0] != None:
                        mylist.insert('0',i[3])
                list_label.config(text='Translated')
            else:
                for i in c.fetchall():
                    if i[0] != None:
                        mylist.insert('0',i[0])
                list_label.config(text='New words')
        else:
            if is_translated == False:
                for i in c.fetchall():
                    if i[2] != None:
                        mylist.insert('0',i[3])
                list_label.config(text='Translated')
            else:
                for i in c.fetchall():
                    if i[2] != None:
                        mylist.insert('0',i[2])
                list_label.config(text='Learnt words')

    def destroy():
        global is_set,is_deletechanging_word_entry,changing_word_submit,cancel_button
        is_set,is_delete = False,False
        infobar.config(text='Welcome to your dictionary')
        cancel_button.grid_forget()
        if changing_word_entry.winfo_ismapped():
            changing_word_entry.grid_forget()
            changing_word_submit.grid_forget()
    

    cancel_button = cancel_button = ttk.Button(button_frame,text='Cancel',command = lambda: destroy())
    changing_word_entry = changing_word_entry = ttk.Entry(set_widgets_frame,width=22,font = ('Helvetica',15))
    changing_word_submit = changing_word_submit = ttk.Button(set_widgets_frame,text = 'Submit', command =lambda: update_word())
    
    cancel_button.grid_forget()
    changing_word_entry.grid_forget()
    changing_word_submit.grid_forget()

    def recycle():
        pass

    def delete_toggle():
        global is_delete,cancel_button,is_set
        is_delete,is_set = True,False
        if is_delete == True: 
            if not cancel_button.winfo_ismapped():
                cancel_button.grid(row =10,rowspan=2,column = 1,columnspan=3,padx=10,pady=10)   
            infobar.config(text='Which word would you like to delete?')
            if changing_word_entry.winfo_ismapped():
                changing_word_entry.grid_forget()
                changing_word_submit.grid_forget()

    def set_toggle():
        global is_set,is_delete,changing_word_entry,changing_word_submit,cancel_button
        is_delete,is_set = False,True
        if is_set == True:
            if not cancel_button.winfo_ismapped():
                cancel_button.grid(row =10,rowspan=2,column = 1,columnspan=3,padx=10,pady=10)     


            infobar.config(text='Which word would you like to set?')
            infobar.grid(row=1,column=4,columnspan=8)


            changing_word_entry.grid(row = 2,columnspan=4, column=5,pady=(25,0),padx=(0,18))
            changing_word_entry.delete('0',tk.END)

            
            changing_word_submit.grid(row=2,column=10,columnspan=2,pady=(25,0))

            def on_enter_key(event):
                changing_word_submit.invoke()
            root.bind('<Return>',on_enter_key)
        
    def on_list_select(event): 
        global cancel_button,is_delete
        if is_delete == True:
            selected_item= mylist.get(mylist.curselection())
            ans = mb.askquestion('delete word',f"Are you sure you want to delete {selected_item}  ?")
            if ans == 'yes':
                mylist.delete(mylist.curselection())
                c.execute("DELETE FROM words WHERE New_word = ? OR Learnt_word = ? OR Translation_of_the_word = ?", (selected_item, selected_item, selected_item))
                conn.commit()

                cancel_button.grid_forget()
                infobar.config(text='Welcome to your dictionary')
                is_delete = False

    scrollbar = ttk.Scrollbar(root)
    scrollbar.grid(row=2, column=19, rowspan=19, sticky='nsew')

    mylist = tk.Listbox(root, yscrollcommand = scrollbar.set, selectbackground="#a6a6a6", selectforeground="black", exportselection=False, height=19,width=30, selectmode="single", bg="#f0f0f0", relief="flat", bd=0, font=('Helvetica', 19))

    mylist.grid(row=2, column=17, rowspan=19, sticky='nsew',pady = (20,0))
    mylist.bind("<<ListboxSelect>>", on_list_select)
    
    scrollbar.config( command = mylist.yview )

    def switch_on_off():
        global is_learnt,is_translated
        is_learnt,is_translated = not is_learnt,True
        if is_learnt == True:
            list_label.config(text = 'Learnt words')
        else:
            list_label.config(text = 'New words')
        if is_learnt == True:
            mylist.delete(0,tk.END)
            c.execute('SELECT * FROM words')
            conn.commit()

            for line in c.fetchall():
                mylist.insert(0,line[2])    
        else:
            mylist.delete(0,tk.END)
            c.execute('SELECT * FROM words')
            conn.commit()

            for line in c.fetchall():
                mylist.insert(0,line[0])              



    button_exit  = ttk.Button(root, text='<-----',command = main_window)
    button_exit.grid(row=1, column=2,  padx=1, pady=1)

    set_word = ttk.Button(button_frame, text='Set words',command=set_toggle)
    set_word.grid(row=2, rowspan=2, column=2, padx=10, pady=10)

    delete_word = ttk.Button(button_frame, text='Delete words',command=delete_toggle)
    delete_word.grid(row=4, rowspan=2, column=1,  columnspan=3, padx=10, pady=10)

    switch = ttk.Button(button_frame,text = 'switch',command = switch_on_off)
    switch.grid(row=6, rowspan=2, column=1,  columnspan=3, padx=10, pady=10)

    translate_button = ttk.Button(button_frame,text = 'translate',command = translate)
    translate_button.grid(row=8, rowspan=2, column=1,  columnspan=3, padx=10, pady=10)

    recycle_bin = ttk.Button(button_frame,text='Recycle bin',command = recycle)
    recycle_bin.grid(row = 18,column=1,rowspan=2,columnspan=3,padx=10,pady=10)

    list_label = ttk.Label(root, text = 'New words',font = ('Helvetica', 20))#,relief='solid')
    list_label.grid(row = 1, column=17,columnspan=3,sticky='nsew')#,pady(20,0))



    utilities.align_column_and_rows(root)

    c.execute('SELECT * FROM words')
    conn.commit()

    for line in c.fetchall():
        mylist.insert(0,line[0])

def practice():
    for widget in root.winfo_children():
       widget.destroy()

    c.execute('SELECT * FROM words')
    conn.commit()
    iterations = [row[1] for row in c.fetchall()]
    global translation 
    translation = ''
    words = utilities.get_words(True)

    
    def generate_new_word(event = None):
        global translation
        c.execute('SELECT * FROM words')
        conn.commit()
        whole_table = c.fetchall()
        c.execute('SELECT * FROM words')
        conn.commit()
        if c.fetchone() != None:
            global generate_word
            def generate_word(max_attempts=100):
                for _ in range(max_attempts):
                    word_informations = random.choice(whole_table)
                    word, iterations,translation = word_informations[0], word_informations[1], word_informations[3]
                    
                    if word is not None:
                        return word,iterations,translation

                mb.showinfo('Congrats','Congratulations! you finished all of the words')
                return None,None,None

            word,iterations,translation = generate_word()
            if word is None:
                main_window()
            c.execute(f"UPDATE words SET Number_of_iterations = {iterations+1} WHERE New_word = '{word}'")
            conn.commit()
    
            word_indicator.config(text = word)
            iteration_indicator.config(text = iterations+1)
            
            if (iterations+1) %5 == 0:
                answer = mb.askquestion('did you learn?', f"you practised the word {word} {iterations+1} times. Did you learn?")
                if answer == 'yes':
                    c.execute(f"UPDATE words SET Learnt_word = '{word}' WHERE New_word = '{word}'")  
                    c.execute(f"UPDATE words SET New_word = NULL WHERE New_word = '{word}'")   
                    conn.commit()
        else:
          mb.showerror('Error','You should add some words first')
    utilities.align_column_and_rows(root)

    generatre_word_label_frame = tk.Frame(root, width=550, height=100)
    generatre_word_label_frame.grid(row=4, column=7, columnspan=5, sticky='nsew')
    generatre_word_label_frame.grid_propagate(0)

    press_enter_label = tk.Label(root, text='Press enter for generating new word', font=('Helvetica', 20))
    press_enter_label.grid(row=1, column=7)  # Adjusted the column index,Ə

    word_label = ttk.Label(generatre_word_label_frame, text='word', font=('Helvetica', 30))
    word_label.grid(row=0, column=0, padx=(50, 25), pady=(25, 25))  # Adjusted the row index

    word_indicator = ttk.Label(generatre_word_label_frame, text="", font=('Helvetica', 20))
    word_indicator.grid(row=0, column=1, padx=(25, 25), sticky='nsew')  # Adjusted the row and column indices

    translate_button = ttk.Button(root, text='Translate',command = lambda: word_indicator.config(text=translation))
    translate_button.grid(row=4, column=12, sticky='e')  # Adjusted the column index

    iterations_frame = ttk.Frame(root, width=400, height=100)
    iterations_frame.grid(row=5, column=7, columnspan=5, sticky='nsew')
    iterations_frame.grid_propagate(0)

    iteration_indicator = ttk.Label(iterations_frame, text="", font=('Helvetica', 20))
    iteration_indicator.grid(row=0, column=6, rowspan=3, columnspan=3)  # Adjusted the row index

    iteration_label = ttk.Label(iterations_frame, text='Iterations', font=('Helvetica', 25))
    iteration_label.grid(row=0, column=3, padx=(25, 25))  # Adjusted the row index

    button_exit = ttk.Button(root, text='<-----', command=main_window)
    button_exit.grid(row=1, column=2, padx=1, pady=1, sticky='nsew')

    root.bind('<Return>',generate_new_word)

def main_window():
    for widget in root.winfo_children():
        widget.destroy()

    label = tk.Label(root, text='Language learning', font=('Helvetica', 30))
    label.grid(row=2, column=0, columnspan=19, sticky='nsew', pady=(20, 0))


    # Buttons with enhanced appearance
    style = ttk.Style()
    style.configure("TButton", font=('Helvetica', 14), padding=10)
    
    button1 = ttk.Button(root, text='Practice',command=practice)
    button1.grid(row=4, rowspan=2, column=3, columnspan=3, sticky='nsew', padx=10, pady=10)

    button2 = ttk.Button(root, text='Add new words', command = Add)
    button2.grid(row=7, rowspan=2, column=3, columnspan=3, sticky='nsew', padx=10, pady=10)

    button5 = ttk.Button(root, text='Settings')
    button5.grid(row=7, rowspan=2, column=13, columnspan=3, sticky='nsew', padx=10, pady=10)

    button6 = ttk.Button(root, text='check out the words',command = check)
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

    window_width = 1200
    window_height = 700
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2 -35

    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    main_window()
    root.mainloop()