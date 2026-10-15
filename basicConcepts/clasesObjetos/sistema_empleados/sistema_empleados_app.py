from empresa import Empresa
from empleado import Empleado
#Pruebas para probrar el siste de mepleados
print('*** Sistema de empleados ***')

#Crear instancia d euna empresa
empresa1 = Empresa('Empresa No 1')
empresa1.contratar_empleado('Pedro Sanchez', 'Ventas')
empresa1.contratar_empleado('Camilo Rodriguez', 'Ventas')
empresa1.contratar_empleado('Felipe Rojas', 'Tecnologia')
empresa1.contratar_empleado('Maria Perez', 'Tecnologia')
empresa2 = Empresa('Empresa No 2')
empresa2.contratar_empleado('Oscar', 'Marketing')


#Cantidad de mepleados en Ventas
print(f'Cantidad de empleados en Ventas: {empresa1.obtener_numero_empleados_departamento('Ventas')}')
print(f'Cantidad total de empleados: {Empleado.contador_empleado}')
print(f'Empleados totales de {empresa1.nombre}: {empresa1.obtener_total_empleados()}')
