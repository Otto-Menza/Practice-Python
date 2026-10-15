#Manejo de cadenas

#Dividir una cadena con split()
cadena = 'Hola Mundo'
palabras = cadena.split('M')
print(palabras)

#Buscar con find
posicion = cadena.find('Mundo')
print(f'Posicion del inicio de la palabra "Mundo": {posicion}')

#Reemplazar con replace
nueva_cadena = cadena.replace('Mundo', 'Parce')
print(f'Nueva cadena con replace: {nueva_cadena}')

#multiplicacion de cadenas:
cadena2 = 'Hola '
nueva_cadena_multipicada = cadena2 * 3
print(f'Cadena multiplicada: {nueva_cadena_multipicada}')

#rmilinar saltos d elinea o espacio en blanco strip(). Quita espacios al inicio y al final
cadena_con_espacios = '   Hola  Que tal  ..'
nueva_cadena_sin_espacios = cadena_con_espacios.strip()
print(f'Cadena sin espacios: {nueva_cadena_sin_espacios}')