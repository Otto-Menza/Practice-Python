print('*** Generadores en Pytho ***')
#es una funcion especial qiue devielve una secuencia de valores uno a uno utiizando la palabra clase yield en lugar de return

def generador(maximo):
    contador = 0
    while contador < maximo:
        yield contador
        contador += 1
# Creamos un generador
var_generador = generador(5)

#Iteramos sobre elñ generador
for valor in var_generador:
    print(valor)