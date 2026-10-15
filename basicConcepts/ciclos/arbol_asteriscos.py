#Arbol Asteriscos
asteriscos = ''
lineas = int(input('Ingresa la cantidad de linas del arbol: '))
for linea in range(1, lineas+1):
    espacios_blanco = ' ' * (lineas-linea)
    asteriscos = '*'*(2 * linea - 1)
    print(espacios_blanco, asteriscos)
