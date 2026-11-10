# Clase servicio snack
import os.path

from basicConcepts.manejoArchivos.maquina_snacks.snack import Snack


class ServicioSnacks:
    NOMBRE_ARCHIVO = 'snacks.txt'
    #Definimos nuestro constructor
    def __init__(self):
        self.snacks = []
        #Revisar si ya existe el archivo de snacks .txt
        #Si ya existe, obtenemos los snacks
        if os.path.isfile(self.NOMBRE_ARCHIVO):
            self.snacks = self.obtener_snacks()
        #y si no existe, creamos el archivo, con unos snacks.
        else:
            self.cargar_snacks_iniciales()

    def obtener_snacks(self):
        snacks = []
        try:
            with open(self.NOMBRE_ARCHIVO, 'r') as archivo:
                for linea in archivo:
                    # 1,'papas',1300
                    id_snack, nombre, precio = linea.strip().split(',')
                    snack = Snack(nombre, precio)
                    snacks.append(snack)
        except Exception as e:
            print(f'Error al leer archivos de snacks: {e}')
        return snacks

    def cargar_snacks_iniciales(self):
        snacks_iniciales = [
            Snack('papas', 3500),
            Snack('Agua', 2500),
            Snack('Chocorramo', 3700)
        ]
        self.snacks.extend(snacks_iniciales)
        self.guardar_snacks_archivo(snacks_iniciales)

    def guardar_snacks_archivo(self, snacks):
        try:
            #iniciamos con with los procesos frente al archivo
            with open(self.NOMBRE_ARCHIVO, 'a') as archivo:
                #Por cada snack se escrbira en la lista, se usa 'a' de append para añadir.
                for snack in snacks:
                    #Se escribe llamando el metodo de escribir que solo llama la informacion en formato simple
                    archivo.write(f'{snack.escribir_snack()}\n')

        except Exception as error:
            print(f'Hubo un error al guardar snacks en archivo: {error}')

    def agregar_snack(self, snack):
        #se agrega en snack a  alista de snacks
        self.snacks.append(snack)
        #y se guarda el snack en el acrhivo.
        self.guardar_snacks_archivo([snack])

    def mostrar_snacks(self):
        print('--- Snacks en el inventario ---')
        for snack in self.snacks:
            print(snack)

    def get_snack(self):
        return self.snacks