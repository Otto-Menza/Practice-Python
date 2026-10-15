# Lista de suscriptores con Set

#Para crear un set vacio usamos el funcion set:
suscriptores = set()
numero_suscriptores = int(input('Ingresa cantidad de suscriptores que vas a agregar: '))

#se usa _ para indicar que el indice de la coleccion y que no se va a usar
for _ in range(numero_suscriptores):
    nuevo_suscriptor = input('Correo de nuevo suscriptor: ')
    while nuevo_suscriptor in suscriptores:
        print(f'Suscriptor {nuevo_suscriptor} Ya existe')
        nuevo_suscriptor = input('Correo de nuevo suscriptor: ')
    suscriptores.add(nuevo_suscriptor)

print(f'Lista actual de suscriptores: {suscriptores}')
salir = False

while not salir:
    print(f'''Menu de suscriptores
        1) Agregar suscriptor
        2) Eliminar suscriptor
        3) Ver lista de suscriptores
        4) salir
        ''')
    opcion = int(input('Ingresa una opción: '))
    if opcion == 1:
        nuevo_suscriptor = input('Correo de nuevo suscriptor: ')
        while nuevo_suscriptor in suscriptores:
            print(f'Suscriptor {nuevo_suscriptor} Ya existe')
            nuevo_suscriptor = input('Correo de nuevo suscriptor: ')
        suscriptores.add(nuevo_suscriptor)
    elif opcion == 2:
        eliminar_suscriptor = input('Correo de suscriptor a eliminar: ')
        while eliminar_suscriptor not in suscriptores:
            print(f'Suscriptor {eliminar_suscriptor} NO existe')
            eliminar_suscriptor = input('Correo de suscriptor a eliminar: ')
        suscriptores.remove(eliminar_suscriptor)
    elif opcion == 3:
        contador = 1
        for suscriptor in suscriptores:
            print(f'{contador}) {suscriptor}')
            contador += 1
    elif opcion == 4:
        print('Saliendo del sistema...')
        salir = True

