import tkinter as tk
from tkinter import ttk

#Creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva ventana')
ventana.configure(background='#1d2d44')

#Etiquetas - crear
etiqueta = ttk.Label(ventana, text='Saludando!')

#Cambiar el texto usando metodo configure
etiqueta.configure(text='Despidiendo...')

#Cambiar el texto con la llave text
etiqueta['text'] = 'Adios'

#Publicacom el componente
etiqueta.pack(pady=20) #Se empaqueta la etiqueta. se movio 20px hacia abajo.







#hacemos visible la ventana
ventana.mainloop()