# Manejo de Tuplas
from time import process_time_ns

mi_tupla = (1,2,3,4,5)
print(mi_tupla)
# No se puede modificar tuplas, ni agregar, ni eliminar elementos. como una constante pero de listas.
#iterar en tuplas:
for elemento in mi_tupla:
    print(elemento)

#Acceder e elementos en tuplas:
print(f'Elemento 2 del indice 1: {mi_tupla[1]}')

#tupla unitaria /  de un solo elemento
tupla_unitaria = 10, #debe tener una coma
print(f'Tupla de un solo elemento: {tupla_unitaria}')

#Tupla anidada: una tupla de tuplas:
tupla_anidada = (1, (2,3), (3,4,5))
print(tupla_anidada)