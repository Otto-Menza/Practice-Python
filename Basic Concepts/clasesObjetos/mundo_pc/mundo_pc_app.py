from raton import Raton
from teclado import Teclado
from monitor import Monitor
from computadora import Computadora
from orden import Orden
monitor1 = Monitor('Sansung', 23)
teclado1 = Teclado('Gamer', 'USB')
raton1 = Raton('HP', 'USB')
computadora1 = Computadora('HP seria 10k', monitor1, teclado1, raton1)

monitor2 = Monitor('San....', 23)
teclado2 = Teclado('Gamer...', 'USB')
raton2 = Raton('HP...', 'USB')
computadora2 = Computadora('HP buena...', monitor2, teclado2, raton2)
computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
print(orden1)

computadora3 = Computadora('PC gamer', monitor2, teclado1, raton2)
orden1.agregar_computadora(computadora3)
print(orden1)