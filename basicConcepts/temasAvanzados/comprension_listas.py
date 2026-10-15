#Comprensión de listas
print('*** Comprensión de listas ***')

#Filtrar solo los pares y generar una lista aparte
numeros = range(1, 10+1)

#SIN USAR coprensión de listas
numeros_pares = []
#Iterar cada elelemento
for numero in numeros:
    if numero % 2 == 0:
        numeros_pares.append(numero)
print(f'Numero pares: {numeros_pares}')

# USANDO  comprensión de listas
## el resultado genera por si ismo una nueva lista: sintaxis: nuela_lista = [expresion for elemento in iterable if]
numeros_impares = [numero for numero in numeros if numero % 2 != 0] #Como solo se esta recuperando el numeor impar, la expresion es solo el numero
print(f'Numeros impares: {numeros_impares}')
