#Repeticion de mensaje
mensaje = input('ingresa un mensaje: ')
repeticiones_mensaje = int(input('Cuantas veces queires que se repita el mensaje?: '))
for i in range(repeticiones_mensaje):
    print(f'{i+1} - {mensaje}')