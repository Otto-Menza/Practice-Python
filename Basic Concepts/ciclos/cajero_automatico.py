#Cajero automatico con While;
print('*** Bienvenido al Cajero automatico Otto ***')
saldo = 1000
salir = False
while not salir:
    print(f'''Lo que puedes hacer:
    1. Retirar
    2. Depositar
    3. Conocer saldo
    4. Salir\n
    ''')
    opcion = int(input('¿Que quieres hacer ahora?: '))
    if opcion == 1:
        monto_retirar = int(input('Ingresa el monto a Retirar: $'))
        if monto_retirar <= saldo and monto_retirar > 0:
            saldo -= monto_retirar
            print(f'Has retirado: ${monto_retirar} | Nuevo saldo: ${saldo}\n')
        else:
            print('Ingresa un monto valido\n')
    elif opcion ==2:
        monto_depositar = int(input('Ingresa el monto a Depositar: $'))
        if monto_depositar > 0 and monto_depositar < 100000:
            saldo += monto_depositar
            print(f'Has depositado: ${monto_depositar} | Nuevo saldo: ${saldo}\n')
        else:
            print('Ingresa un valor entre 0 y 999999\n')
    elif opcion == 3:
        print('Tu Saldo es: $',saldo)
    elif opcion == 4:
        print('Estas saliendo del sistema. Hasta pronto!')
        salir = True
    else:
        print('Elige una opcion valida\n')
else:
    print('Ha terminaedo el Ciclo')