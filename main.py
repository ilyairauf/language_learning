import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter.messagebox import showinfo as msg
from tkinter import messagebox as mb
import time
import random
import utilities

conn = sqlite3.connect('database.db')
c = conn.cursor()



def Add():
    for widget in root.winfo_children():
       widget.destroy()
    
    utilities.align_column_and_rows(root)
    
    button_exit  = ttk.Button(root, text='<-',command = main_window)
    button_exit.grid(row=1, column=2,  padx=1, pady=1)

    Entry = ttk.Entry(root, font=('Helvetica', 25),width=35)
    Entry.grid(row=2, column=2,columnspan = 10,)
    
    def Add_database():
        data = Entry.get()
        words = utilities.get_words(True)
        if data and not data.isspace() and data not in words and len(data)<27:
            conn = sqlite3.connect('database.db')
            c = conn.cursor()
            c.execute(f'INSERT INTO words (New_word,Number_of_iterations) VALUES(?,?)',(data,0))
            conn.commit()
            conn.close()
            msg = ttk.Label(root,text = 'Your word succesfully added!',font=('Helvetica', 15))
            msg.grid(row=3,column=3)
            Entry.delete('0','end')
        elif data in words:
            mb.showwarning('word exist','this word already exists in your dictionary')
        elif len(data)>=27:
            mb.showerror('lenght error', "Your word can't be longer than 27 letters")
    button_submit  = ttk.Button(root, text='submit',command = Add_database)
    button_submit.grid(row=2, column=17,  padx=1, pady=1)

    def on_enter_key(event):
        button_submit.invoke()
    root.bind('<Return>',on_enter_key)

def check():

    for widget in root.winfo_children():
       widget.destroy()  
    
    button_frame = tk.Frame(root,width=200,height=300,padx=15)
    button_frame.grid(row=2, column=2,  padx=1, pady=1)
    button_frame.grid_propagate(0)

    set_widgets_frame = tk.Frame(root,width=470,height=400)
    set_widgets_frame.grid(row = 1,columnspan=5,column=4,rowspan=2)
    set_widgets_frame.grid_propagate(0)

    global is_delete,is_set,is_learnt
    is_delete,is_set,is_learnt= False,False,False
      
    infobar = ttk.Label(set_widgets_frame, text='Welcome to your dictionary',font = ('Helvetica', 20))
    infobar.grid(row = 1, column = 8,columnspan=3,pady=(30,0))
    
    def delete_toggle():
        global is_delete
        def destroy():
            global is_delete
            is_delete = not is_delete
            infobar.config(text='Welcome to your dictionary')
            cancel_button.destroy()

        if is_delete == False and is_set == False:
            is_delete = not is_delete
            global cancel_button
            cancel_button = ttk.Button(button_frame,text='Cancel',command = destroy)
            cancel_button.grid(row = 8,rowspan=2,column = 1,columnspan=3,padx=10,pady=10)   
            infobar.config(text='Which word would you like to delete?')

    def set_toggle():
        global is_set

        def destroy():
            global is_set
            is_set = not is_set
            infobar.config(text='Welcome to your dictionary')
            cancel_button.destroy()
            changing_word_entry.destroy()
            changing_word_submit.destroy()


        if is_delete == False and is_set == False:
            is_set = not is_set
            global cancel_button
            cancel_button = ttk.Button(button_frame,text='Cancel',command = destroy)
            cancel_button.grid(row = 8,rowspan=2,column = 1,columnspan=3,padx=10,pady=10)   

            def update_word():
                if mylist.curselection() == ():
                    mb.showwarning('choose a word','You have to choose a word from list first')
                else:
                    selected_index = mylist.curselection()
                    updated_word = changing_word_entry.get()
                    words = utilities.get_words(True) + utilities.get_words(False)
                    if updated_word != '' and updated_word not in words:
                        c.execute(f"UPDATE words SET New_word = '{updated_word}' WHERE New_word = '{mylist.get(selected_index)}'")
                        conn.commit()
                        c.execute(f"UPDATE words SET Learnt_word = '{updated_word}' WHERE Learnt_word = '{mylist.get(selected_index)}'")
                        conn.commit()
                        mylist.delete(selected_index)
                        mylist.insert(selected_index,updated_word)
                        changing_word_entry.destroy()
                        changing_word_submit.destroy()
                        infobar.config(text="Welcome to your dictionary")
                        global cancel_button,is_set
                        cancel_button.destroy()
                        is_set = False

                    elif updated_word in words:
                        mb.showerror('word already exist', "Sorry you can't update a word to an existing one")



            infobar.config(text='Which word would you like to set?')
            infobar.grid(row=1,column=4,columnspan=8)

            changing_word_entry = ttk.Entry(set_widgets_frame,width=22,font = ('Helvetica',15))
            changing_word_entry.grid(row = 2,columnspan=4, column=5,pady=(25,0),padx=(0,18))
    
            changing_word_submit = ttk.Button(set_widgets_frame,text = 'Submit',command = update_word)
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
                c.execute("DELETE FROM words WHERE New_word = ?", (selected_item,))
                conn.commit()
                c.execute("DELETE FROM words WHERE Learnt_word = ?", (selected_item,))
                conn.commit()
                cancel_button.destroy()
                infobar.config(text='Welcome to your dictionary')
                is_delete = False

        if is_set == True:
            pass 

    scrollbar = ttk.Scrollbar(root)
    scrollbar.grid(row=2, column=20, rowspan=19, sticky='nsew')

    mylist = tk.Listbox(root, yscrollcommand = scrollbar.set, selectbackground="#a6a6a6", selectforeground="black", exportselection=False, height=19, selectmode="single", bg="#f0f0f0", relief="flat", bd=0, font=('Helvetica', 19))

    mylist.grid(row=2, column=19, rowspan=19, sticky='nsew',pady = (20,0))
    mylist.bind("<<ListboxSelect>>", on_list_select)
    
    scrollbar.config( command = mylist.yview )

    def switch_on_off():
        global is_learnt
        is_learnt = not is_learnt
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
    
    words = utilities.get_words(True)
    
    def generate_new_word():
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
                    word, iterations = word_informations[0], word_informations[1]
                    if word is not None:
                        return word,iterations

                mb.showinfo('Congrats','Congratulations! you finished all of the words')
                return None,None

            word,iterations = generate_word()
            if word is None:
                main_window()
            c.execute(f"UPDATE words SET Number_of_iterations = {iterations+1} WHERE New_word = '{word}'")
            conn.commit()
    
            word_indicator.config(text = word)
            iteration_indicator.config(text = iterations+1)
            
            #if (iterations+1) %5 == 0:
            #    answer = mb.askquestion('did you learn?', f"you practised the word {word} {iterations+1} times. Did you learn?")
            #    if answer == 'yes':
            #        c.execute(f"UPDATE words SET Learnt_word = '{word}' WHERE New_word = '{word}'")  
            #        c.execute(f"UPDATE words SET New_word = NULL WHERE New_word = '{word}'")   
            #        conn.commit()
        else:
          mb.showerror('Error','You should add some words first')
    utilities.align_column_and_rows(root)

    generatre__word_label_frame = tk.Frame(root,width=550,height=100)#,borderwidth=2,relief='solid')
    generatre__word_label_frame.grid(row = 4,column = 7,columnspan=5,sticky='nsew')
    generatre__word_label_frame.grid_propagate(0)

    word_label = ttk.Label(generatre__word_label_frame,text='word',font= ('Helvetica', 30))
    word_label.grid(row = 1,column = 3,padx=(50,25),pady=(25,25))

    word_indicator = ttk.Label(generatre__word_label_frame,text = "",font= ('Helvetica', 20))
    word_indicator.grid(row = 1,column=7,padx = (25,25),sticky='nsew')

    generate_button = ttk.Button(root,text = 'Generate',command = generate_new_word)
    generate_button.grid(row=4,column=15,sticky='e')

    iterations_frame = ttk.Frame(root,width = 400,height=100)#,borderwidth=2,relief="solid")
    iterations_frame.grid(row = 5,column = 7,columnspan=5,sticky='nsew')
    iterations_frame.grid_propagate(0)
    
    iteration_indicator = ttk.Label(iterations_frame,text = f"",font= ('Helvetica', 20))
    iteration_indicator.grid(row=7,column=10,rowspan=3,columnspan=3)

    iteration_label = ttk.Label(iterations_frame,text='Iterations',font=('Helvetica', 25))
    iteration_label.grid(row = 7,column=7,padx = (25,25))

    button_exit = ttk.Button(root, text='<-----',command = main_window)
    button_exit.grid(row=1, column=2,  padx=1, pady=1,sticky='nsew')

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

    window_width = 1000
    window_height = 700
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    main_window()
    root.mainloop()


