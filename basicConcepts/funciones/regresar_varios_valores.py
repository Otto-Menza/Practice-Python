# Regresar una tupla de valores desde una función:
# definicion de una funcion:
def personla_mayusculas(nombre, apellido, edad):
    #De esta forma retorna una tupla de valores:
    return nombre.upper(), apellido.upper(), edad

nombre, apellido, edad = personla_mayusculas('Sandra', 'Rodriguez', 23)
print(f'Persona: {nombre} {apellido}, {edad} años')


#Ejmplo coordenadas:
def obtener_coordenadas():
    #Para el ejemplo definimos las varibales, datos quemados
    x,y,z = 10, 20, 30
    #retorna una tupla
    return x, y, z
#llamar la funcion:
resultado = obtener_coordenadas()
print(resultado)

#Unpacking de la tupla:
x1, y1, z1 = resultado
print(f'cord X = {x1} - cord Y = {y1} - cord Z = {z1}')