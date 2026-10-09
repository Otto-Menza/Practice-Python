#Clase de empleado
class Empleado:
    #atribbuto de clase
    contador_empleado = 0

    #Constructor de la clase
    def __init__(self, nombre, departamento):
        Empleado.contador_empleado += 1
        self._id = Empleado.contador_empleado
        self._nombre = nombre
        self._departamento = departamento

    @property #Metodod get
    def id(self):
        return self._id
    @id.setter #Metoddo set
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def departamento(self):
        return self._departamento
    @departamento.setter
    def departamento(self, departamento):
        self._departamento = departamento

    @classmethod #metodo de clase
    def obtener_total_empleados(cls):
        return cls.contador_empleado