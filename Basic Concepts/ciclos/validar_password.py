#validar contraseña
password_valid = False
while not password_valid:
    print(f'''Validando password!!''')
    password = input('Ingresa una contraseña (minimo 6 caracteres): ')
    if len(password) >= 6:
        print('Contraseña Valida!')
        password_valid = True
    else:
        print('Contraseña invalida - intenta de nuevo!\n')