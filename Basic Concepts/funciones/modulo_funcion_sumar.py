#Modulos: ej: funcion sumar:

#Funcion de suma
def suma(a,b):
    resultado = a+b
    return  resultado
def restar(a,b):
    resultado = a-b
    return resultado

#Prueba de sumar:
#Para que esta prueba no se ejecute si usamos este modulo en otro lado entonces:
if __name__ == '__main__':
    print(f'Prueba de suma desde el modulo: {suma(5,5)}')