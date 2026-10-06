# Argumentos por llave valor (key, value) = Keyword Arguments (son en forma de diccionario)
print('*** Argumentos varibles en forma de diccionario ***')
#Se debe respetar el orden, primero args y dpeues kwargs
def superheroe(nombre, *args, **kwargs):
    print(f'Superheroe: {nombre} - {args} - Más info: {kwargs}')
#llamna de la funcion:
superheroe('spiderman', 'super fuerza', 'telaraña', edad=28, ciudad='New York')
#los argumentos y los keyword arguments son opcinales:
superheroe('Otto', personalidad='buena onda')
