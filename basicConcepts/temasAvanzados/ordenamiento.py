print('*** Ordenamiento en python ***')

#MEtodo sorted(iterable, key=None, reverse=False)

empleados = ['Juan', 'Pedro', 'Maria']
empleados_ordenados = sorted(empleados)
print(f'Por defecto orden de forma alfabetica A-Z: {empleados_ordenados}')
#DE forma descendente:
empleados_ordenados_za = sorted(empleados, reverse=True)
print(f'Por defecto orden de forma alfabetica Z-A: {empleados_ordenados_za}')

#Ordena run diccionario, proporcionanado una llave
empleados_dic = [
    {'nombre': 'Juan', 'salario': 3000},
    {'nombre': 'Maria', 'salario': 2000},
    {'nombre': 'Pedro', 'salario': 2500},
    {'nombre': 'Andres', 'salario': 6000}
]
empleados_ordenados_por_salario = sorted(empleados_dic, key=lambda x: x['salario'], reverse=True)
print(f'EMpleaados ordenados por salario: {empleados_ordenados_por_salario}')