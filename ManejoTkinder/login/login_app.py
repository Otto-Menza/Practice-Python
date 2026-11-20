import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

#Creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Nueva ventana')
ventana.configure(background='#1d2d44')

#Configuracion del grid:
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

#estilos paquete de estilos
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure(ventana, background='#1d2d44', foreground='white', fieldbackground='black')
estilos.configure('TButton', background='#0D5f73')
estilos.map('TButton', background=[('active', '#0a9396')])

#Agregamos un frame (contenedor)
frame = ttk.Frame(ventana)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=3)

#titulo
etiqueta = ttk.Label(frame, text='Login', font=('Arial', 20))
etiqueta.grid(row=0, column=0, columnspan=2)

#Usuario
usuario_etiqueta = ttk.Label(frame, text='Usuario: ')
usuario_etiqueta.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)

#input usuario:
usuario_caja_texto = ttk.Entry(frame)
usuario_caja_texto.grid(row=1, column=1, sticky=tk.E, padx=5, pady=5)

#COntraseña
contrasena_etiqueta = ttk.Label(frame, text='Contraseña: ')
contrasena_etiqueta.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)

#input contraseña:
contrasena_caja_texto = ttk.Entry(frame, show='*')
contrasena_caja_texto.grid(row=2, column=1, sticky=tk.E, padx=5, pady=5)

#Boton
login_boton = ttk.Button(frame, text='Enviar')
login_boton.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

def validar(event=None):
    usuario = usuario_caja_texto.get()
    contrasena = contrasena_caja_texto.get()
    if usuario == 'root' and contrasena == 'admin':
        showinfo(title='Login', message='Iniciando sesion')
    else:
        showerror(title='Login', message='Datos invalidos')

#Asociar eventos al boton
login_boton.bind('<Return>', validar) #capturando el evento de clic
login_boton.bind('<Button-1>', validar) # clieck izquierdo del mouse

#publicacion del frame:
frame.grid(row=0, column=0)


#hacemos visible la ventana
ventana.mainloop()