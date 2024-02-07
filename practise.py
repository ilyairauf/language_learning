import tkinter as tk
from tkinter import ttk
import sqlite3
import utilities
import random
from tkinter import messagebox as mb




class Practise:

        
    def practice(root,callback):
        for widget in root.winfo_children():
           widget.destroy()

        c,conn = utilities.connection()
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
            print(whole_table)
            if c.fetchone() != None:
                global generate_word
                def generate_word(max_attempts=100):
                    for _ in range(max_attempts):
                        word_informations = random.choice(whole_table)
                        word, iterations,translation,delete_integer = word_informations[0], word_informations[1], word_informations[3],word_informations[4]

                        if word is not None and delete_integer !=0:
                            return word,iterations,translation

                    mb.showinfo('Congrats','Congratulations! you finished all of the words')
                    return None,None,None

                word,iterations,translation = generate_word()
                if word is None:
                    callback(root)
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
                        number_of_words.config(text = f"remaining words {len(utilities.get_words(True))}") 
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

        button_exit = ttk.Button(root, text='<-----', command=lambda: callback(root))
        button_exit.grid(row=1, column=2, padx=1, pady=1, sticky='nsew')

        number_of_words = ttk.Label(root, text = f"remaining words {len(words)}", font = ('Helvetica', 20))
        number_of_words.grid(row = 3,column = 3)

        root.bind('<Return>',generate_new_word)
