from computadora import  Computadora

#Clase Orden:
class Orden:
    contador_orden = 0
    #constructor / inicializador
    def __init__(self, computadoras):
        Orden.contador_orden += 1
        self.id_orden = Orden.contador_orden
        self.computadoras = computadoras

    def agregar_computadora(self, computadora):
        self.computadoras.append(computadora)

    def __str__(self):
        computadoras_str = ('')
        for computadora in self.computadoras:
            computadoras_str += '\n' + computadora.__str__() #COmo no se esta usando el metodo sprint se usa __str__
        return (f'''Orden # {self.id_orden}
        Computadores: {computadoras_str}''')

#Programa principal
