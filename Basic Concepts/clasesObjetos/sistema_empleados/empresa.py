from empleado import Empleado
#Class de empresa
class Empresa:
    def __init__(self, nombre):
        self._nombre = nombre
        self._empleados = []

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    #metodos de la Clase Empresa
    def contratar_empleado(self, nombre, departamento):
        empleado = Empleado(nombre, departamento)
        self._empleados.append(empleado)

    def obtener_numero_empleados_departamento(self, departamento):
        contador_empleado_por_departamento = 0
        for empleado in self._empleados:
            if empleado.departamento == departamento:
                contador_empleado_por_departamento += 1
        return contador_empleado_por_departamento

    def obtener_total_empleados(self):
        for empleado in self._empleados:
            print(f'Empleado {empleado.id} - {empleado.nombre}, Departamento: {empleado.departamento}')
        return len(self._empleados)