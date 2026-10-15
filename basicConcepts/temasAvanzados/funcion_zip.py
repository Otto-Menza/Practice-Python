#Funcion zip
##Es la union de 2 iterables, es una tupla.

nombres = ['Pedro', 'Rocio', 'Fernando']
edades = [20, 25, 30, 52]
ciudades = ['Bogota', 'medellin', 'Tunja']

#Combinar los elementos, usnado funcion zip:
personas = zip(nombres, edades, ciudades) # crea las tuplas partiendo de la lista/itrable mas corto, el resto se ignora

## Genera un objeto entones si usamos el metodo sprint llamaremos la ubicacion en memoria.
print(personas)
#Iterar el objeto tras un zip:
for persona in personas:
    print(persona)