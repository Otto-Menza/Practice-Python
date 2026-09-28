# Lista de suscriptores con Set
suscriptores = {'julianqemail.com', 'paglo@email.com', 'fer@email.com'}
print(f'Lista actual de suscriptores: {suscriptores}')

#Agregar nuevo suscriptor:
nuevo_suscriptor = 'Fer@email.com'
if nuevo_suscriptor in suscriptores:
    print(f'Suscriptor {nuevo_suscriptor} ya existe!')
else:
    suscriptores.add(nuevo_suscriptor)
    print('Nuevo suscriptor agregado')
    print(suscriptores)

#eliminar suscriptor
eliminar_suscriptor = 'Fer@email.com'
if nuevo_suscriptor in suscriptores:
    suscriptores.remove(eliminar_suscriptor)
    print(f'Suscriptor Eliminado')
else:
    print('Suscriptor NO existe')

print(f'Lista: {suscriptores}')

#Cantidad de suscriptores
print(f'Canditdad de suscriptores: {len(suscriptores)}')