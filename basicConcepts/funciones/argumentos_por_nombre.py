#LLamando funciones por nombre de argumentos:

#creamos la funcion:
def iprimir_persona(nombre, apellido, edad):
    print(f'Persona: {nombre} {apellido}, {edad} años')
#llamamos por nombre, no importa el orden:
iprimir_persona(apellido='Gonzalez', nombre='Pedro', edad=45)

#declarar parametros con valores por default:
def imprimir_persona(nombre='', apellido='', edad=0):
    print(f'Persona: {nombre} {apellido}, {edad} años')
#llamamos por nombre, no importa el orden:
imprimir_persona(apellido='Rosales')