print('*** Suma de aergumentos variables ***')

#funcion de sumar:
def sumar(*args):
    total = 0
    for numero in args:
        total += numero
    return total

resultado = sumar(3,4,3,2,2,3,4,3,3,3,3)
print(f'La suma total es: {resultado}')