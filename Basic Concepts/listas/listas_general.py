# Manejo de listas
mi_lista = [1,2,3,4,5]
print(f'{mi_lista} --> Lista original')

#metodo len para saber el largo/tamaño d ela lista
print(f'Tamaño de lista: {len(mi_lista)}')

# Accedor a los elementos de una lista con el indice:
print(f'Acceder al elemento del indice 2: {mi_lista[0]}')
print(f'Accedor el ultim indice: {mi_lista[-1]}')

#Cambiar valor de elemento segun indice
mi_lista[1]=10
print(f'Cambiano el elemento dle indice 2: {mi_lista}')

#Agregar elementos a la lista:
mi_lista.append(6)
print(f'Nuevo elemento en lista, al final: {mi_lista}')

#Añadir un nuevo elemento en un indice especifico.
mi_lista.insert(2,15)
print(f'Se inserta elemento 15 en el indica 2: {mi_lista}')

#Eliminar elementos:
#Metodo remove: elimina un elemento, busca el elemento, no el indice. Elimina 1 solo elemento, asi esten diplicados
mi_lista.remove(15)
print(f'Se elimino el elemento 15 del indice 2: {mi_lista}')

#eliminar por indice:
# ---- metodo pop ----
mi_lista.pop(3)
print(f'Se elimino el elemento 4 del indice 3: {mi_lista}')
# ---- metodo del -----
del mi_lista[2]
print(f'Se elimino el elemento 3 de indice 2: {mi_lista}')

#Generar sublistas
sublista = mi_lista[1:3] #una sublista tomando el indica 1, 2 omitiendo el 3 de la lista original
print(f'Sublista del indice 1 y 2: {sublista}')