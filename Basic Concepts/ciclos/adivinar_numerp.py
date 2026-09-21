#Juego de Adivinar Número
import random
numero_secreto = random.randint(1,50)
opcion_usuario = int(input('Ingresa un numero del 1 al 50: '))
intentos = 1
print(numero_secreto)
while numero_secreto != opcion_usuario and intentos < 8:
    if numero_secreto > opcion_usuario:
        opcion_usuario = int(input('Casi lo logras, es más arriba, intenta otra vez: '))
    else:
        opcion_usuario = int(input('Casi lo logras, es más abajo, intenta otra vez: '))
    intentos += 1
else:
    if numero_secreto == opcion_usuario:
        print(f'Buen trabajo!, el número era: {numero_secreto}, y usaste {intentos} intentos!')
    else:
        print('Buen intento, pero se agotaron los 8 intentos')