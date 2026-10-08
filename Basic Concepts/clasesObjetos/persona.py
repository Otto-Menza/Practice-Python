#Definicion d euna clase:
#El nombre d elas clases se definene con la priemra letra mayuscula, y cada separaion de palabras con la priemra letra mayuscula: PascalCase
class Persona:

    #Constructor:
    def __init__(self, nombre, apellido):
        #Creamos los stributos d
        self.nombre = nombre
        self.apellido = apellido

    #Inicialiamos la clase, solo para endtener el concepto, pero normlamente se iniciliza con el constructor (arriba)
    # def inicializar_persona(self, nombre, apellido1):
    #     #Agregamos los atributos de la clase, y los inicializamos buenas practicas: mismo nombre
    #     self.nombre = nombre
    #     self.apellido = apellido1

    def mostrar_persona(self):
        print(f'''Persona:
        Nombre: {self.nombre}
        Apellido: {self.apellido}''')
        print(f'Direccion de memoria de Self: {id(self)}')


#Creacion de objetos | unicamente que se ejecute en este archivo
if __name__ == '__main__':
    #creacion dle primer objeto (partiendo d ela inicizalizacion de la clase):
    # persona1 = Persona() #Se crea objeto vacio
    # persona1.inicializar_persona('Laila', 'Gonzales') #Se asigna valores a los parametros de nombre y apellido
    # persona1.mostrar_persona()

    #Ahora para crear un objeto de la clase Persona, como ya hemos definido el constructor, es asi:
    persona1 = Persona('Layla', 'Acosta')
    persona1.mostrar_persona()
    print(f'Direccion de memoria Persona 1: {id(persona1)}')

    #Crear segundo objeto:
    persona2 = Persona('Ian', 'Sanchez')
    persona2.mostrar_persona()
    print(f'Direccion de memoria persona 2: {id(persona2)}')
