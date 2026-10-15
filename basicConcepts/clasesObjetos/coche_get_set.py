#Clase coche para ver el cocepto de encaptulamiento:
class Coche:
    def __init__(self, marca, modelo, color):
        self._marca = marca # Aributo protegido
        self._modelo = modelo # Atributo protegido
        self._color = color # Atributo protegido

    def conducir(self):
        print(f'''El coche:
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')

    #Definimos los metodos get y set de cada atributo
    # def get_marca(self):
    #     return self._marca
    @property #Con este operador podmeos defir el metodo get de forma más pythonica
    def marca(self):
        return self._marca
    @marca.setter #Con este operador podmeos defir el metodo SET de forma más pythonica
    def marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo
    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_color(self):
        return self._color
    def set_color(self, color):
        self._color = color


#Programa principal
if __name__ == '__main__':
    coche1 = Coche('AION', '2026', 'Dorado')
    coche1.conducir()
    # No deberiamos poder acceder a los atributos que no sean publicos:
    #coche1.set_marca('AIon 2')
    coche1.set_modelo('2026 2')
    coche1.set_color('Dorado 2')
    coche1.conducir()
    #Usando los nuevos metodos get y set:
    print(f'Llamando el metodo get desde el nuevo metodo marca: {coche1.marca}')
    coche1.marca = 'Aion 3' #Queda ifual escrito a como se le llamaria sin usar encapsulamiento, peor si lo estamos haciendo.
    print(f'Llamando el metodo get desde el nuevo metodo marca: {coche1.marca}')

    #Agregar nuevos atributos, podmeos usar este metodo para agregar un atributo solo a un objeto epecifico
    setattr(coche1, 'precio', 20000)
    print(f'El nuevo atributo del coche1 es precio que es = {coche1.precio}')
    ## Otra forma de crear nuevos atributos a un objeto especifico:
    coche1.version = 'full equipo'
    print(f'El nuevo atributo del coche1 es version que es = {coche1.version}')
    #Como no tenemos en el metodo d ela clase los atributos nuevos, podmeos iprimir o ver los atributos del objeto asi:
    print(f'Atributos del coche1: {coche1.__dict__}')