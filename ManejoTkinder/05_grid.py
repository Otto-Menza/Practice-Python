import tkinter as tk
from tkinter import ttk

#Creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva ventana')
ventana.configure(background='#1d2d44')

#Manejo de Grid
boton1 = ttk.Button(ventana, text='Boton1')
boton2 = ttk.Button(ventana, text='Boton2')
boton3 = ttk.Button(ventana, text='Boton3')

#componenetes de forma horizontal
boton1.grid(row=0, column=0, sticky=tk.NS, pady=20, padx=20) #margen con pad
boton2.grid(row=0, column=1, sticky=tk.NSEW)
boton3.grid(row=0, column=2, sticky=tk.NW, ipadx=20, ipady=20) #paddng con ipad

#Configurar el grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)
ventana.columnconfigure(2, weight=1)

ventana.rowconfigure(0, weight=1)
ventana.rowconfigure(1, weight=1)
ventana.rowconfigure(2, weight=1)

#componenetes en forma vertical
# boton1.grid(row=0, column=0)
# boton2.grid(row=1, column=0)
# boton3.grid(row=2, column=0)

#COmponentes en diagonal
# boton1.grid(row=0, column=0)
# boton2.grid(row=1, column=1)
# boton3.grid(row=2, column=2)

#hacemos visible la ventana
ventana.mainloop()