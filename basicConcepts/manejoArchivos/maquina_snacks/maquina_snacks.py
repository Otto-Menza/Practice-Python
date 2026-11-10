from basicConcepts.manejoArchivos.maquina_snacks.servicio_snack import ServicioSnacks
from basicConcepts.manejoArchivos.maquina_snacks.snack import Snack


class MaquinaSnacks:
    def __init__(self):
        self.servicio_snacks = ServicioSnacks()
        self.productos = []

    def maquina_snacks(self):
        salir = False
        print("*** Maquina de Snacks ***")
        self.servicio_snacks.mostrar_snacks()
        while not salir:
            try:
                opcion = self.mostrar_menu()
                salir = self.ejecutar_opcion(opcion)
            except Exception as e:
                print(f'Error: {e}')

    def mostrar_menu(self):
        print(f'''Menu de Maquina de Snacks
        1. Comprar snack
        2. Mostrar ticket
        3. Agregar Nuevo Snack al Inventario
        4. Mostrar Inventario de Snacks
        5. Salir''')
        return int(input('Ingresa una opción: '))

    def ejecutar_opcion(self, opcion):
        if opcion == 1:
            self.comprar_snack()
        elif opcion == 2:
            self.mostrar_ticket()
        elif opcion == 3:
            self.agregar_snack()
        elif opcion == 4:
            self.servicio_snacks.mostrar_snacks()
        elif opcion == 5:
            print('Cerrando sistema')
            return True
        else:
            print(f'Opción invlaida: {opcion}')
        return False

    def comprar_snack(self):
        id_snack = int(input('Ingresa ID del snack para agregar: '))
        snacks = self.servicio_snacks.get_snack()
        snack = next((snack for snack in snacks if snack.id_snack == id_snack), None)
        if snack:
            self.productos.append(snack)
            print(f'Se agrego | {snack} | a la lista')
        else:
            print(f'Id ingresado no encontrado: {id_snack}')

    def mostrar_ticket(self):
        if not self.productos:
            print('No hay snacks en el ticket')
            return
        total = sum(int(snack.precio) for snack in self.productos)
        print('--- Ticket de Venta ---')
        for producto in self.productos:
            print(f'\t- {producto.nombre} - ${producto.precio}')
        print(f'\tTotal -> ${total}')

    def agregar_snack(self):
        nombre = input('Nombre del Snack: ')
        precio = float(input('Precio del snack: '))
        try:
            nuevo_snack = Snack(nombre, precio)
            self.servicio_snacks.agregar_snack(nuevo_snack)
            print('Snack Agregado correctamente')
        except Exception as e:
            print(f'Error añ agregar snack: {e}')

if __name__ == '__main__':
    maquina_snacks = MaquinaSnacks()
    maquina_snacks.maquina_snacks()