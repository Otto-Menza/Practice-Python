#Operador mas +
cadena1 = "Hola"
cadena2 = "mundo"
cadena3 = cadena1 + ' ' + cadena2
print(cadena1+cadena2)
print(cadena3)

# Usando el metodo Join
concatenacion = ''.join([cadena1,' ',cadena2])
#Es necesario crear una lista vacia para que al llamar al elemento "join" esta ocupe ese espacio
print(concatenacion)