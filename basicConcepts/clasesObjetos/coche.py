#Clase coche para ver el cocepto de encaptulamiento:
class Coche:
    def __init__(self, marca, modelo, color):
        self.marca = marca # Aributo publico
        self._modelo = modelo # Atributo protegido
        self.__color = color # Atributo provado

    def conducir(self):
        print(f'''El coche:
        Marca: {self.marca}
        Modelo: {self._modelo}
        Color: {self.__color}''')

#Programa principal
if __name__ == '__main__':
    coche1 = Coche('AION', '2026', 'Dorado')
    coche1.conducir()
    # No deberiamos poder acceder a los atributos que no sean publicos:
    coche1.marca = 'Aion 2'
    coche1._modelo = '2026 2' #Aun en python/pycharm s epeuda, esto no deberia hacerce = mala practica, porque es protegido
    coche1.__color = 'Dorado 2' # Como es provado no permite cambiarlo. se peude ede esta forma:
    coche1._Coche__color = 'Dorado 2' # NO es buena practica
    coche1.conducir()