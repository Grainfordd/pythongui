mport tkinter as tk
from tkinter import ttk
    
win = tk.Tk()

def click_me():
    action.configure(text = f'Hello {name.get()} {number_chosen.get()}')

ttk.Label(win, text='Enter a name').grid(column=0)

# Addings a Texbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

# Adding a button
action = ttk.Button(win, text='Click Me!', command=click_me)
action.grid(column=2, row=1)

ttk.Label(win, text='Choose a number').grid(column=1, row=0)
number = tk.StringVar()

# Se le añade el state para que no se pueda elegir otro valor
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = 1, 2, 4, 42, 100
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

#--------- Creando 3 checkButtons ------------------
chVarDis = tk.IntVar()
check2 = tk.Checkbutton(win, text='Disabled', variable=chVarDis, state='disabled')
check2.deselect()
check2.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text='Unchecked', variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text='Enabled', variable=chVarEn)
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)

name_entered.focus() # Poner el cursor en el cuadro de texto cuando se inicie la aplicación

win.mainloop()
