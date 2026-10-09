# Clase de libro
class Libro:
    contador_libro = 0
    #Crear el constructor
    def __init__(self, titulo, autor, genero):
        Libro.contador_libro += 1
        self._id = Libro.contador_libro
        self._titulo = titulo
        self._genero = genero
        self._autor = autor

    @property #Medoto get
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        self._id = id

    @property #Metodod get
    def titulo(self):
        return self._titulo
    @titulo.setter #metodo set
    def titulo(self, titulo):
        self._titulo = titulo

    @property
    def autor(self):
        return self._autor
    @autor.setter
    def autor(self, autor):
        self._autor = autor

    @property
    def genero(self):
        return self._genero
    @genero.setter
    def genero(self, genero):
        self._genero = genero