# Calculadora basica cpn while
resultado = 0
salir = False
while not salir:
    print(f'''¿Que operación quieres hacer?
    1. Sumar
    2. Restar
    3. Dividir
    4. Multiplicar
    5. Salir
    ''')
    opcion = int(input('Indica la operación: '))
    if opcion == 1:
        operador_uno = float(input('Ingresar el primero valor: '))
        operador_dos = float(input('Ingresar el segundo valor: '))
        print(f'La Suma es: {operador_uno}+{operador_dos} = {operador_dos + operador_uno}')
    elif opcion == 2:
        operador_uno = float(input('Ingresar el primero valor: '))
        operador_dos = float(input('Ingresar el segundo valor: '))
        print(f'La Resta es: {operador_uno}-{operador_dos} = {operador_uno - operador_dos}')
    elif opcion == 3:
        operador_uno = float(input('Ingresar el primero valor: '))
        operador_dos = float(input('Ingresar el segundo valor: '))
        print(f'La División es: {operador_uno}/{operador_dos} = {operador_uno / operador_dos}')
    elif opcion == 4:
        operador_uno = float(input('Ingresar el primero valor: '))
        operador_dos = float(input('Ingresar el segundo valor: '))
        print(f'La Multiplicación es: {operador_uno}*{operador_dos} = {operador_uno * operador_dos}')
    elif opcion == 5:
        print('Saliendo de la calculadora... Hasta pronto!')
        salir = True
    else:
        print('Indica una opcion valida!')