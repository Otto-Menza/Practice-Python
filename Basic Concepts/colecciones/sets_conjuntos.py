# Sets en python

#Sets o conjunto se crea con {} y no tiene el concepto de indice.
mi_set = {1,2,3,4,5,5,5}
#Al imprimir no imprime los valores repetidos. Como no tienen orden pueden imprimirse en orden diferente.
print(mi_set)

#SI se peuden agregar elementos a los sets.
mi_set.add(6)
mi_set.add(7)
print(mi_set)

#Eliminar elementos
mi_set.remove(4) #Se elimina el valor, NO pr indice pues no cuenta cpn indice.

#Iterar los elementos del set:
for elemento in mi_set:
    print(elemento, end=' ')

#Coprobar si existe un elemento en el set
print(f'\nExiste el valor de 4 en el set?: {4 in mi_set}')

#Conocer la ongitud del conjunto
print(f'Longitud del Set: {len(mi_set)}')