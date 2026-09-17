# inmutabilidad de cadenas

cadena1 = "Hola mundo"
print(cadena1)
# cadena1[0] = 'h'
# print(cadena1)
# No se puede cambiar los caracteres dentro de las cadenas que ya han sido creadas, lo que s epuede hacer es crear una nueva
cadena2 = cadena1
# para que un objeto no sea eliminado se debe guardar en otra variable.
cadena1 = 'adios'
print(cadena1)
print(cadena2)