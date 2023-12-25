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

word_list = [
    ("fəsil", 0, None, "계절", 0),
    ("yaz", 0, None, "봄", 0),
    ("yay", 0, None, "여름", 0),
    ("payız", 0, None, "가을", 0),
    ("qış", 0, None, "겨울", 0),
    ("soyuq", 0, None, "춥다", 0),
    ("isti", 0, None, "덥다", 0),
    ("mülayim / sərin", 0, None, "따뜻하다 /시원하다", 0),
    ("həmişə", 0, None, "항상/늘", 0),
    ("gözəl", 0, None, "아름답다 / 예쁘다", 0),
    ("dağ / dağaçıxma", 0, None, "산/ 등산", 0),
    ("makyaj etmək", 0, None, "화장하다", 0),
    ("acılı", 0, None, "맵다", 0),
    ("ağır", 0, None, "무겁다", 0),
    ("kömək etmək", 0, None, "돕다", 0),
    ("univermaq", 0, None, "백화점", 0),
    ("ayaqqabı", 0, None, "구두", 0),
    ("boyfriend/girlfriend", 0, None, "남자 친구 /여자 친구", 0),
    ("sual vermək", 0, None, "질문하다", 0),
    ("bugünlərdə, son günlərdə", 0, None, "요즘", 0),
    ("tez-tez", 0, None, "자주", 0),
    ("qar yağmaq", 0, None, "눈이 오다/ 내리다", 0),
    ("yağış yağmaq", 0, None, "비가 오다/내리다", 0),
    ("açıq/ tutqun", 0, None, "맑다 /흐리다", 0),
    ("külək əsmək", 0, None, "바람이 불다", 0),
    ("tez-tez", 0, None, "자주", 0),
    ("keçən qış", 0, None, "지난 겨울", 0),
    ("metro stansiyası", 0, None, "지하철역", 0),
    ("dəniz", 0, None, "바다", 0),
    ("xəzan", 0, None, "단풍", 0),
    ("papaq", 0, None, "모자", 0),
    ("snow board", 0, None, "스노보드", 0),
    ("kirşə, xizək (oturub sürülən)- sleigh/…를 타다", 0, None, "눈썰매", 0),
    ("qaradamı", 0, None, "눈사람", 0),
    ("qartopu oynamaq", 0, None, "눈싸움 /눈싸움을 하다", 0),
    ("xizək kurortu", 0, None, "스키장", 0),
    ("çimərlik", 0, None, "해수욕장", 0),
    ("vadi", 0, None, "계곡", 0),
    ("teatr", 0, None, "극장", 0),
    ("aeroport", 0, None, "공항", 0),
    ("karaoke", 0, None, "노래방", 0),
    ("tutqun", 0, None, "흐리다", 0),
    ("bazar", 0, None, "시장", 0),
    ("çiy balıq yeməyi", 0, None, "회", 0),
    ("həddən artıq", 0, None, "무척", 0),
    ("Koreyada dağ (Soraq dağı)", 0, None, "설악산", 0),
    ("yenidən, təkrar / görüşənədək, yenə görüşərik", 0, None, "또 / 또 만나요", 0),
    ("bugünlərdə, son günlərdə", 0, None, "요즘", 0),
    ("makaronlu yemək adı", 0, None, "막국수", 0),
    ("bu il", 0, None, "올해", 0),
    ("biraz", 0, None, "조금", 0),
    ("güllərə baxmaq", 0, None, "꽃구경", 0),
    ("açıq hava, çöl, bayır", 0, None, "야외", 0),
    ("açmaq(gül)", 0, None, "피다", 0),
    ("xüsusilə", 0, None, "특히", 0),
    ("sakura çiçəkləri", 0, None, "벚꽃", 0),
    ("seulda yer adı", 0, None, "여의도", 0),
    ("festival", 0, None, "축제", 0),
    ("çimərlik", 0, None, "해수욕장", 0),
    ("Əyalətin", 0, None, "강원도", 0),
    ("Şəhər adı", 0, None, "속초", 0),
    ("Busanda çimərlik", 0, None, "해운대", 0),
    ("dağ adı", 0, None, "지리산", 0),
    ("Qar;göz", 0, None, "눈", 0)
]


#c.executemany('INSERT INTO words VALUES (?,?,?,?,?)',word_list)
#conn.commit()




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
            c.execute(f'INSERT INTO words (New_word,Number_of_iterations,translation_of_the_word,deleted) VALUES(?,?,?,?)',(word_entry_value,0,word_translation_value,0))
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
            button_exit.config(command=main_window)
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
        
    def destroy():
        is_set,is_delete = False,False
        infobar.config(text='Welcome to your dictionary')
        if changing_word_entry.winfo_ismapped():
            changing_word_entry.grid_forget()
            changing_word_submit.grid_forget()





    

    cancel_button = cancel_button = ttk.Button(button_frame,text='Cancel',command = lambda: destroy())
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
            ans = mb.askquestion('delete word',f"Are you sure you want to delete {selected_item}  ?")
            if ans == 'yes':
                mylist.delete(mylist.curselection())
                c.execute("UPDATE words SET deleted =  ? WHERE New_word = ? OR Learnt_word = ? OR Translation_of_the_word = ?", (1,selected_item, selected_item, selected_item))             
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
            
            if (iterations+1) %3 == 0:
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