from basicConcepts.colecciones.tuplas import elemento

print('**funcion sum y Next **')

lista = [1,2,3,4,5]

resultado = sum(lista)
print(f'Resultado de la suma: {resultado}')

#podmeos dalre un valor inicar para la suma:
resultado2 = sum(lista, 20)
print(f'Resultado con valor inicial: {resultado2}')

#Funcion Next()
iterador = iter(lista) #convertimos la lista en un iterable
#objtenemos el proximo elemento del iterador usando la funcion next
print(f'Siguiente elemento del iterable (1): {next(iterador)}')
print(f'Siguiente elemento del iterable (2): {next(iterador)}')
print(f'Siguiente elemento del iterable (3): {next(iterador)}')
print(f'Siguiente elemento del iterable (4): {next(iterador)}')
print(f'Siguiente elemento del iterable (5): {next(iterador)}') #si se pasa d elos elementos iterables manda error.