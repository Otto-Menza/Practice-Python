import tkinter as tk
from tkinter import ttk

#Creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva ventana')
ventana.configure(background='#1d2d44')

def mostrar():
    texto = caja_texto.get() #recuperar el texto en la caja
    print(f'Teto en caja: {texto}')
    etiqueta['text'] = texto

#caja de texto
caja_texto = ttk.Entry(ventana, font=('Arial', 15))
caja_texto.pack(pady=20)


#Agregar boton
boton = ttk.Button(ventana, text='Enviar', command=mostrar)
boton.pack()

#Etiqeuta
etiqueta = ttk.Label(ventana, text='Valor inicial')
etiqueta.pack(pady=20)



#hacemos visible la ventana
ventana.mainloop()