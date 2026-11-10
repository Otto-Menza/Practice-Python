from basicConcepts.manejoArchivos.catalogo_peliculas.pelicula import Pelicula
from basicConcepts.manejoArchivos.catalogo_peliculas.servicio_peliculas import ServicioPeliculas

class AppCatalogoPeliculas:
    def __init__(self):
        self.servicio_peliculas = ServicioPeliculas()

    def motrar_menu(self):
        print('*** App Catalogo de Peliculas ***')
        while True:
            try:
                print('''Opciones:
                1. Agregar Pelicula
                2. Listar Peliculas
                3. Eliminar catalogo de peliculas
                4. Salir''')
                opcion = int(input('Escribe un valor entre 1 y 4: '))
                if opcion == 1:
                    nombre_pelicula = input('Ingresa el nombre:')
                    pelicula = Pelicula(nombre_pelicula)
                    self.servicio_peliculas.agregar_peliculas(pelicula)
                elif opcion == 2:
                    self.servicio_peliculas.listar_peliculas()
                elif opcion == 3:
                    self.servicio_peliculas.eliminar_archio_peliculas()
                elif opcion == 4:
                    print('Saliendo del programa...')
                    break
                else:
                    print('Opcion invalida, introduce un valor entre 1 y 4')
            except ValueError:
                print('Error: introduce un número valido, 1-4')
            except Exception as e:
                print(f'Hay un error: {e}')

if __name__ == '__main__':
    app = AppCatalogoPeliculas()
    app.motrar_menu()