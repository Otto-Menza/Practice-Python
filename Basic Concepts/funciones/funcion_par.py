print('*** funcion Par ***')

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
numero = int(input('Ingresa un número: '))
print(f'El número es par?: {es_par(numero)}')