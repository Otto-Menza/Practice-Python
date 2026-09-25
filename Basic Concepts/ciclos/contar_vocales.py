# Declarar la variable
cadena = "Hola Mundo"
contador = 0
# Agregar el ciclo for
for letra in cadena:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador += 1
# Imprimir la cantidad de vocales encontradas en la cadena
print(contador)