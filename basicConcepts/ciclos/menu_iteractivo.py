#menú iterativo:
print('*** Menú iteractivo ***')

salir = False
while not salir:
    print(f'''Menu:
    1: Crear Cuenta
    2. Eliminar Cuenta
    3. Salir \n
    ''')
    opcion = int(input('Escoje una opción: '))
    if opcion == 1:
        print('Creando cuenta... \n')
    elif opcion == 2:
        print('Eliminando cuenta... \n')
    elif opcion == 3:
        print('Saliendo del sistema...')
        salir = True
    else:
        print('Selecciona una opción valida\n')