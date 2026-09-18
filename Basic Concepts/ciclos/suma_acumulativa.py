#Suma acumulativa con While, sumar del 1 al 5
contador = 1
suma=0
while contador<=5:
    print(f'suma # {contador}: {suma} + {contador} = {suma + contador}')
    suma += contador
    contador += 1
print(f'La suma total es: {suma}')