#Clase servicoio de pelicula
import os

from basicConcepts.manejoArchivos.catalogo_peliculas.pelicula import Pelicula

class ServicioPeliculas:
    NOMBRE_ARCHIVO = 'peliculas.txt'

    def agregar_peliculas(self, pelicula):
        with open(self.NOMBRE_ARCHIVO, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    def listar_peliculas(self):
        with open(self.NOMBRE_ARCHIVO, 'r', encoding='utf8') as archivo:
            print('--- Peliculas em el inventario ---')
            #Imprimir todo el contenido del archivo
            print(archivo.read())

    def eliminar_archio_peliculas(self):
        os.remove(self.NOMBRE_ARCHIVO)
        print(f'Archivo eliminado: {self.NOMBRE_ARCHIVO}')