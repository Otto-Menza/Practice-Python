## Leer archivo

nombre_archivo = 'mi_archivo.txt'

# leer usnado readlines()
with open(nombre_archivo, 'r') as archivo:
    #Leer todas las lineas
    #print(archivo.readlines()) #Una lista con cada una de las lineas del archivo
    #Podemos iterar las lineas:
    lineas = archivo.readlines()
    for linea in lineas:
        print(linea.strip()) #Usamos metodo strip para quitar los espacios, saltos d elinea al final de cada linea

#Leertodo el conteniod con read
print('\nLeyendo todo el contenido con read')
with open(nombre_archivo, 'r') as archivo:
    print(archivo.read())