import tkinter as tk
from tkinter import ttk
import sqlite3
import utilities
from tkinter import messagebox as mb

global c,conn
c,conn = utilities.connection()

class Check:

    def check(root,callback):

        

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

        c.execute('SELECT * FROM words')
        conn.commit()

        for widget in root.winfo_children():
           widget.destroy()  

        button_frame = tk.Frame(root,width=200,height=550,padx=15)#,borderwidth=2,relief='solid')
        button_frame.grid(row=2, column=2,  padx=1, pady=1)
        button_frame.grid_propagate(0)

        set_widgets_frame = tk.Frame(root,width=470,height=600)#,borderwidth=2,relief='solid')
        set_widgets_frame.grid(row = 1,columnspan=5,column=4,rowspan=2)
        set_widgets_frame.grid_propagate(0)

        global is_delete,is_set,is_learnt,is_translated,cancel_button,changing_word_entry,changing_word_submit,is_deleted,infobar
        is_delete,is_set,is_learnt,is_translated,is_deleted= False,False,False,True,False


        infobar = ttk.Label(set_widgets_frame, text='Welcome to your dictionary',font = ('Helvetica', 20))
        infobar.grid(row = 0, column = 8,columnspan=3)



        def recycle():
            global changing_word_entry,changing_word_submit,cancel_button,infobar
            mylist.delete(0,tk.END)
            if changing_word_entry.winfo_ismapped:
                changing_word_entry.grid_forget()
                changing_word_submit.grid_forget()
                cancel_button.grid_forget()
            button_exit.config(command=lambda: exit())

            def delete():
                selected_item= mylist.get(mylist.curselection())
                ans = mb.askquestion('delete word',f"Are you sure you want to delete {selected_item}  ?")
                if ans =='yes':
                    word = mylist.get(selected_index)
                    c.execute('DELETE FROM words WHERE New_word = ? OR Learnt_word = ?',(word,word))
                    conn.commit()
                    mylist.delete(selected_index)
            def restore():
                word = mylist.get(selected_index)
                c.execute('UPDATE words SET deleted = ? WHERE New_word = ? OR Learnt_word = ?',(0,word,word))
                conn.commit()
                mylist.delete(selected_index)
            popup_menu = tk.Menu(tearoff=0)
            popup_menu.add_command(label = "delete",command = delete)
            popup_menu.add_command(label = "restore",command = restore)

            def right_click(event):
                global selected_index
                selected_index = mylist.nearest(event.y)
                mylist.selection_clear(0, tk.END)
                mylist.selection_set(selected_index)
                mylist.see(selected_index)
                try:
                    popup_menu.tk_popup(event.x_root, event.y_root, 0)
                finally:
                    popup_menu.grab_release()  

            set_word.grid_forget()
            switch.grid_forget()
            delete_word.grid_forget()
            translate_button.grid_forget()
            recycle_bin.grid_forget()
            infobar.config(text='you can right click on items for change')
            c.execute('SELECT * FROM words')
            conn.commit()
            for line in c.fetchall():
                if line[4] == 1:
                    if line[0] == None:
                        mylist.insert(0,line[2])     
                    else:
                        mylist.insert(0,line[0])
            recycle_bin.config(text = 'New words') 
            list_label.config(text='Deleted words')

            def exit():
                switch.grid(row=6, rowspan=2, column=1,  columnspan=3, padx=10, pady=10)
                delete_word.grid(row=4, rowspan=2, column=1,  columnspan=3, padx=10, pady=10)
                set_word.grid(row=2, rowspan=2, column=2, padx=10, pady=10)
                translate_button.grid(row=8, rowspan=2, column=1,  columnspan=3, padx=10, pady=10)
                recycle_bin.grid(row = 18,column=1,rowspan=2,columnspan=3,padx=10,pady=10)
                infobar.config(text='Welcome to your dictionary')
                c.execute('SELECT * FROM words')
                conn.commit()
                for line in c.fetchall():
                    if line[4] == 0:
                        mylist.insert(0,line[0])
                recycle_bin.config(text = 'Recycle bin') 
                list_label.config(text='New words')
                button_exit.config(command=lambda: callback(root))
            root.bind("<Button-3>", right_click)
    
        def translate():
            if is_deleted:
                mb.showerror('deleted','if you want to see the translation you have to recover it.')
            else:
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



        cancel_button = cancel_button = ttk.Button(button_frame,text='Cancel',command = lambda: utilities.destroy(is_set,is_delete,infobar,changing_word_entry,changing_word_submit,cancel_button))
        changing_word_entry = changing_word_entry = ttk.Entry(set_widgets_frame,width=22,font = ('Helvetica',15))
        changing_word_submit = changing_word_submit = ttk.Button(set_widgets_frame,text = 'Submit', command =lambda: update_word())

        cancel_button.grid_forget()
        changing_word_entry.grid_forget()
        changing_word_submit.grid_forget()

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
                mylist.delete(mylist.curselection())
                c.execute('SELECT * FROM words')
                conn.commit()
                whole_table = c.fetchall()
                
                print(whole_table,selected_item)
                c.execute("UPDATE words SET deleted =  ? WHERE New_word = ? OR Learnt_word = ? OR Translation_of_the_word = ?", (1,selected_item, selected_item, selected_item))             
                conn.commit()
                c.execute('SELECT * FROM words')
                conn.commit()
                whole_table = c.fetchall()
                
                print(whole_table,selected_item)
                cancel_button.grid_forget()
                infobar.config(text='Welcome to your dictionary')
                is_delete = False

        scrollbar = ttk.Scrollbar(root)
        scrollbar.grid(row=2, column=19, rowspan=19, sticky='nsew')

        mylist = tk.Listbox(root, yscrollcommand = scrollbar.set, selectbackground="#a6a6a6", selectforeground="black", exportselection=False, height=19,width=30, selectmode="single", bg="#f0f0f0", relief="solid",borderwidth = 2, bd=0, font=('Helvetica', 19))

        mylist.grid(row=2, column=17, rowspan=19, sticky='nsew',pady = (20,0))
        mylist.bind("<<ListboxSelect>>", on_list_select)

        scrollbar.config( command = mylist.yview )

        def switch_on_off():
            global is_learnt,is_translated
            is_learnt,is_translated = not is_learnt,True
            if is_learnt == True:
                list_label.config(text = 'Learned words')
            else:
                list_label.config(text = 'New words')
            if is_learnt == True:
                mylist.delete(0,tk.END)
                c.execute('SELECT * FROM words')
                conn.commit()

                for line in c.fetchall():
                    if line[4] == 0:
                        mylist.insert(0,line[2])    
            else:
                mylist.delete(0,tk.END)
                c.execute('SELECT * FROM words')
                conn.commit()

                for line in c.fetchall():
                    if line[4] == 0:
                        mylist.insert(0,line[0])              



        button_exit  = ttk.Button(root, text='<-----',command = lambda: callback(root))
        button_exit.grid(row=1, column=2,  padx=1, pady=1)

        set_word = ttk.Button(button_frame, text='Set words',command=set_toggle)
        set_word.grid(row=2, rowspan=2, column=2, padx=10, pady=10)

        delete_word = ttk.Button(button_frame, text='Delete words',command=delete_toggle)
        delete_word.grid(row=4, rowspan=2, column=1,  columnspan=3, padx=10, pady=10)

        switch = ttk.Button(button_frame,text = 'switch',command = switch_on_off)
        switch.grid(row=6, rowspan=2, column=1,  columnspan=3, padx=10, pady=10)

        translate_button = ttk.Button(button_frame,text = 'translate',command = translate)
        translate_button.grid(row=8, rowspan=2, column=1,  columnspan=3, padx=10, pady=10)

        recycle_bin = ttk.Button(button_frame,text='Recycle bin',command =recycle)
        recycle_bin.grid(row = 18,column=1,rowspan=2,columnspan=3,padx=10,pady=10)

        list_label = ttk.Label(root, text = 'New words',font = ('Helvetica', 20))#,relief='solid')
        list_label.grid(row = 1, column=17,columnspan=3,sticky='nsew')#,pady(20,0))



        utilities.align_column_and_rows(root)

        c.execute('SELECT * FROM words')
        conn.commit()

        for line in c.fetchall():
            if line[4] == 0:
                mylist.insert(0,line[0])
