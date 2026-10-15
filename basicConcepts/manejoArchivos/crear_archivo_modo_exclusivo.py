

print('** abrir un archivo en modo exlusivo ***')

nombre_archivo = 'mi_archivo3.txt'
try:
    with open(nombre_archivo, 'x') as archivo:
        archivo.write('Escritura en modo exlusivo\n')
        archivo.write('Otra linea desde creacion exclusiva')
    print('Se ha creado el archivo')
except FileExistsError as error:
    print(f'El archivo {nombre_archivo} ya existe.. error: {error}')