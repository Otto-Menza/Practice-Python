#Lista y dentro tenemos diccionarios:
#Creamos la lista:

mi_lista = [
    {'nombre':'Regina',
     'apellido': 'Flores',
     'edad': 21
     }]
print(mi_lista)
#Agregar elemento a la lista:
mi_lista.append({
    'nombre':'Alejandro',
    'apellido': 'Reyes',
    'edad': 32
    })
print(mi_lista)

#Acceder a un diccinario desde una lista:
print(f'''
Nombre: {mi_lista[0].get('nombre')}
Apellido: {mi_lista[0].get('apellido')}
Edad: {mi_lista[0].get('edad')}
--------------
Nombre: {mi_lista[1].get('nombre')}
Apellido: {mi_lista[1].get('apellido')}
Edad: {mi_lista[1].get('edad')}
''')

#iterar listas con diccionarios:
#si necesitamos contador podemos usar el metodo enumerate()
print()
for contador, item in enumerate(mi_lista):
    print(f'{contador}) - Persona: {item}')
    #o acceder al detalle de cada item/persona
    print(f'Detalle: Nombre: {item.get('nombre')} {item.get('apellido')}, edad: {item.get('edad')} años')