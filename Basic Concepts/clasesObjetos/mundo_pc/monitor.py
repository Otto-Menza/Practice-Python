#Clase monitor
class Monitor:
    contador_monitor = 0
    #inicialziar clase - constructor
    def __init__(self, marca, tamanio):
        Monitor.contador_monitor += 1
        self.id_monitor = Monitor.contador_monitor
        self.marca = marca
        self.tamanio = tamanio

    def __str__(self):
        return (f'Monitor # {self.id_monitor} - Marca: {self.marca} - Tamaño: {self.tamanio}')

if __name__ == '__main__':
    monitor1 = Monitor('Sansung', '23 plg')
    print(monitor1)

