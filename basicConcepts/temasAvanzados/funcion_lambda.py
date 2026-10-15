#Funciones lambda
#funciones pequeñas y temporales
from functools import reduce

print('*** Funciones Lambda ***')
#FUNCION NORMAL:
def cuadrado(x):
    return x ** 2
print(f'El cuadrado de 5 es: {cuadrado(5)}')

##FUNCION LAMBDA
cuadrado_lambda = lambda x: x ** 2
print(f'El cuadrado de 7 es {cuadrado_lambda(7)}')

#Funcion map | Se usa con iterbles, la funcion map a ejecutarse por cada iteracion y crea un nuevo iterable
numeros = [1,2,3,4,5,6,7,8,9]
numeros_al_cuadrado = list(map(lambda x: x ** 2, numeros))
print(f'Numeros al cuadrado: {numeros_al_cuadrado}')

#Funcion filter y lambda: sirve para generar otro iterable/coleccion desde alun filtro a una coleccion ya existente:
numeros_pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f'Numeros pares usnaod filter: {numeros_pares}')

#Funcion Reduce.. usnado lambda
sumar_acumulativa = reduce(lambda x, y: x+y, numeros) #es para una funcion especifica de 2 argumentos: entocnes primero toma el elemento 1 y el elemento 2 y los suma, depeus toma el resultado de la suma aterior y lo suma con el elemento 3.
print(f'suma acumulativa: {sumar_acumulativa}')