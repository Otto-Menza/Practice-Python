from raton import Raton
from teclado import Teclado
from monitor import Monitor

#Clase de raton
class Computadora():
    contador_computadora = 0
    #definir constructor / inicializador de la clase
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadora += 1
        self.id_computadora = Computadora.contador_computadora
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton

    def __str__(self):
        return (f'''{self.nombre}: {self.id_computadora}
        Monitor: {self.monitor}
        Teclado: {self.teclado}
        Raton: {self.raton}''')

#Porgrama principal
if __name__ == '__main__':
    monitor1 = Monitor('Sansung', 23)
    teclado1 = Teclado('Gamer', 'USB')
    raton1 = Raton('HP', 'USB')
    computadora1 = Computadora('HP seria 10k', monitor1, teclado1, raton1)
    print(computadora1)