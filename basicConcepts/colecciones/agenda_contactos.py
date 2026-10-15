#diccionario de diccionarios

agenda = {
    'Carlos': {
        'telefono': '312254655',
        'email': 'carlos@email.com',
        'direccion': 'cll 123 23 34'
    },
    'Maria': {
            'telefono': '313254655',
            'email': 'maria@email.com',
            'direccion': 'cll 124 23 34'
        },
    'Pedro': {
            'telefono': '314254655',
            'email': 'pedro@email.com',
            'direccion': 'cll 125 23 34'
        }
}
print(agenda)

#Accedor a un contacto especifico:
print(f'''Información de María:
    Teléfono: {agenda['Maria']['telefono']}
    Email: {agenda['Maria']['email']}
    Direccion: {agenda.get('Maria').get('direccion')}
''')

#Agregar nuevo contacto
agenda['Ana'] = {
        'telefono': '316254655',
        'email': 'ana@email.com',
        'direccion': 'cll 127 23 34'
    }
#print(agenda['Ana'])

#eliminar elementos, 2 formas:
print(agenda)
print('')
agenda.pop('Ana')
print(agenda)
print('')
del agenda['Maria']
print(agenda)

#Iterar en el diccinario
for nombre, detalles in agenda.items():
    print(f'''Nombre: {nombre}
    Teléfono: {detalles.get('telefono')}
''')
print(len(agenda))