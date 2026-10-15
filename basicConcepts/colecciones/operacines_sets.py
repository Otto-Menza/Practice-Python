# Operaciones con Set

#Unión de conjuntos
a = {1,2,3,4}
b = {4,5,6,7}
union = a | b
print(f'Union de sets/conjuntos: {union}')

#intersepcion / valores que coinciden:
intersepcion = a & b
print(f'Intercepción a & b: {intersepcion}')

#Diferencia entre conjuntos: los valores que concidan con el conjunto 'b' se quitaran de 'a':
diferencia = a-b
print(f'Diferencia entre a - b: {diferencia}')