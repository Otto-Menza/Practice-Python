# Herencia
## Super Clase / Clase padre
from sys import orig_argv


class Animal:
    def comer(self):
        print('Muchas veces al día')

    def dormir(self):
        print('muchas horas / varias horas')

    def hacer_sonido(self):
        print(('Hcaer algun sonido'))

class Perro(Animal):
    def hacer_sonido(self):
        print('Ladrar')

    def dormir(self):
        print('Duermo 15 goras al día')

class Gato(Animal):
    def hacer_sonido(self):
        print('Maullar')


#Metodo o funcion polimorfica
def hacer_sonido_animal(animal):
    animal.hacer_sonido()


print('*** Ejemplo de Herencia en python ***')
print('Clase padre, soy Animal')
animal1 = Animal()
animal1.dormir()
animal1.comer()

print('\nSoy un perro / Clase Hija')
perro1 = Perro()
perro1.hacer_sonido()
perro1.dormir()

print('\nSoy un Gato / Clase Hija')
gato1 = Gato()
gato1.hacer_sonido()

print('\nSoy un Gato / Clase Hija - usando funcion polimorfica')
hacer_sonido_animal(gato1)
