#clase de Pelicula
class Pelicula:
    contador_pelicula = 0
    #Constructor
    def __init__(self, nombre=''):
        Pelicula.contador_pelicula += 1
        self.id_peliculas = Pelicula.contador_pelicula
        self.nombre = nombre

    def __str__(self):
        return f'{self.id_peliculas}: {self.nombre}'

    def escribir_pelicula(self):
        return f'{self.nombre}'