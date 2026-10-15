# Crear archivo con python

nombre_archivo = 'mi_archivo.txt'

#Abrir el archivo en modo ('w')
archivo = open(nombre_archivo, 'w')
archivo.write('Escribiendo en el archivo')
archivo.write('Escribiendo segudido de la linea anterior\n')
archivo.write('Escribiendo en otra linea\n')
#cerrar eñ archivo, recomendado
archivo.close()

print(f'Se creo el archivo: {nombre_archivo}')

#trabajar con el bloque with para definir y el trabajo del archivo, no es necesario llaamr el metodo close()
nombre_archivo2 = 'mi_archivo2.txt'

with open(nombre_archivo2, 'w') as archivo:  #Se abre el archivo
    archivo.write('Escribiendo en el archivo')
    archivo.write('Escribiendo segudido de la linea anterior')
    archivo.write('\nEscribiendo en otra linea')
print(f'Se creo el archivo: {nombre_archivo2}')