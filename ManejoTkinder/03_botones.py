import tkinter as tk
from tkinter import ttk

#Creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva ventana')
ventana.configure(background='#1d2d44')

def saludar():
    print('Saludando desde el boton')
#Botones
boton1 = ttk.Button(ventana, text='Enviar', command=saludar) #sin parentesis el metodo slaudar para que se ejecute solo al cli
boton1.pack(pady=20)


#hacemos visible la ventana
ventana.mainloop()