print('*** Imprimir detalles de personas ***')

#funcion:
def imprimir_detalle(**kwargs):
    print('\nValores recibidos: ')
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')
#llamada de la funcion
imprimir_detalle(nombre='Oscar', apellido='Perez', edad=34, salario=2000)