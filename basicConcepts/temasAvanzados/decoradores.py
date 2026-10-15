print('** Decoradores **')

#definimos la funcion decorador
def decorador(funcion):
    def wrapper(*args, **kwargs):
        print('Antes de llamar la funcion saludar')
        resultado = funcion(*args, **kwargs)
        print('Despues de llamar la funciona saludar')
        return resultado
    return wrapper

@decorador
def saludar(nombre):
    print(f'Hola {nombre}')

saludar('Carlos')