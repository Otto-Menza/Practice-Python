from libro import Libro
#Clase biblioteca
class Biblioteca:
    #Definir el constructor
    def __init__(self, nombre):
        self._nombre = nombre
        self._libros = []

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def libros(self):
        return self._libros
    @libros.setter
    def libros(self, libros):
        self._libros = libros

    def agregar_libro(self, libro):
        self._libros.append(libro)

    def mostrar_libro(self, libro):
        print(f'Libro => Titulo: {libro.titulo}, Autor: {libro.autor}, Genero: {libro.genero}')

    def buscar_libros_por_autor(self, autor):
        print(f'\nLibros de {autor}:')
        for libro in self._libros:
            if libro.autor.lower() == autor.lower():
                self.mostrar_libro(libro)

    def buscar_libro_por_genero(self, genero):
        print(f'\nLibros del Genero {genero}:')
        for libro in self._libros:
            if libro.genero.lower() == genero.lower():
                self.mostrar_libro(libro)

    def mostrar_todos_los_libros(self):
        print(f'\nTodos los libros de la {self._nombre}:')
        for libro in self._libros:
            self.mostrar_libro(libro)
