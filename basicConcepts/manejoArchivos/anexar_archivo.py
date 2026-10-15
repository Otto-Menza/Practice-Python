print('** anexar info al archivo ***')

nombre_archivo = 'mi_archivo.txt'
with open(nombre_archivo, 'a') as archivo:
    #Anexar al archivo
    archivo.write('Anexando nueco contenido...\n')
    archivo.write('Otra linea anexada\n')
print(f'se ha anexado la info en {nombre_archivo}')
#se va a anexar cada que lo corremos.