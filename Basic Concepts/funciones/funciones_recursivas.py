print('Imprimir del 1 al 5 de forma recursiva')
#definir funcion
def funcion_recursiva(numero):
    #caso base
    if numero == 1:
        print(numero, end=' ') #1
    else : #Caso recursivo
        funcion_recursiva(numero-1)
        print(numero, end=' ')
#llamada a la funcion
funcion_recursiva(5)
print('')

#Calcular factorial
def numero_factorial(numero):
    #Valor base
    if numero == 1 or numero == 1:
        print(f'Resultado factorial de {numero}! es: 1')
        return 1
    else: #caso recursivo
        factorial = numero * numero_factorial(numero-1)
        print(f'Resultado factorial parcial {numero}! es: {factorial}')
        return factorial
numero = 3
resultado = numero_factorial(numero)
print(f'El resultado del factorial de {numero}! es: {resultado}')
print('')

#calculadora d epotencia
def calcular_potencia(base, potencia):
    #valor base
    if potencia == 0:
        return 1
    else: #Caso recursivo:
        potencia_parcial = base * calcular_potencia(base, potencia-1)
        return potencia_parcial
#lamada a la funcion
base = 3
potencia = 3
resultado_potencia = calcular_potencia(base, potencia)
print(f'{base} elevado a la potencia {potencia} es: {resultado_potencia}')