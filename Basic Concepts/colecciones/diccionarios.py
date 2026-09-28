# Diccionarios en Python
#Tambien los diccionarios no aceptan valores duplicados.

persona = {
    'nombre': 'Sergio',
    'edad': 30,
    'ciudad': 'Bogota'
}

#Acceder a los elementos de un diccionario
print(f'Nombre: {persona['nombre']}')
#Otra forma de obtener el valor:
print(f'Edad: {persona.get('edad')}')
print(f'Ciudad: {persona.get('ciudad')}')

#Modificar valor del diccinario:
persona['edad'] = 35
print(f'Nuevo valor Edad: {persona['edad']}')

#Agregar nuevo elemento
persona['profesion'] = 'Ingeniero'
print(f'Nuevo elemento = Profesión: {persona.get('profesion')}')

#Eliminar elemento, llave y valor:
del persona['ciudad']
print(persona)
#Eliminar con metodo pop, al igual que en listas:
persona.pop('profesion')
print(persona)

#Iterar diccionarios:
for llave, valor in persona.items():
    print(f'Llave: {llave}, Valor: {valor}')
#por valores
for valor in persona.values():
    print(f'Valor - {valor}')
for llave in persona.keys():
    print(f'Llave - {llave}')
