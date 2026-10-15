# playlist con listas y ordenar de forma alfabetica
numero_canciones = int(input('Cauntas canciones vas a ingresar: '))
lista_canciones = []
contador_canciones = 1
while contador_canciones <= numero_canciones:
    nombre_cancion = input(f'Canción # {contador_canciones}: ')
    lista_canciones.append(nombre_cancion)
    contador_canciones += 1
lista_canciones.sort()
print(f'Lista de forma alfabetica:{lista_canciones}\n')

#lista de forma descendente alfabeticamente:
lista_canciones.sort(reverse=True)
contador = 1
print('Lista de forma descendente, iterando cada elemento de la lista:')
for cancion in lista_canciones:
    print(f'{contador} - {cancion}')
    contador += 1