#Conceptos generales de funciones
#asi importamos modulos de otros archivos
import modulo_funcion_sumar
#Otra forma es importar directamente la funcion:
from modulo_funcion_sumar import restar

#Funcion saludar

def saludar():
    print('Un saludo desde una función ...')
##llamando la funcion
saludar()

#Parametros
def saludar_parametros(mensaje):
    print(mensaje)
## Llamamos a la funcion con un parametro
saludar_parametros('Saluando desde una funcion con un parametro...')

#Funcion de suma
#Asi usamos funciones de tro modulos
resultado_suma = modulo_funcion_sumar.suma(3,5)
print(f'La suma es: {resultado_suma}')

print(f'Resultado de la resta: {restar(10,3)}')