#Clase aritmetica
class Aritmetica:
    #Se peude crear varios cpnstructores, pero python va a tomar el ultimo que se haya escrito:
    #Definicion del contructor:
    def __init__(self, operando1=None, operando2=None):
        #creamos los atributos:
        self._operando1 = operando1
        self._operando2 = operando2

    #definicion de metodos get y set, de forma pythonica:
    @property #Metodo Get
    def operando1(self):
        return self._operando1
    @operando1.setter #metodo set
    def operando1(self, operando1):
        self._operando1 = operando1

    @property #Metodo get
    def operando2(self):
        return self._operando2
    @operando2.setter #Metodo set
    def operando2(self, operando2):
        self._operando2 = operando2


    def sumar(self):
        print(f'La suma de {self._operando1} + {self._operando2} = {self._operando2 + self._operando1}')
    def resta(self):
        print(f'La resta de {self._operando1} - {self._operando2} = {self._operando2 - self._operando1}')

if __name__ == '__main__':
    #Objeto 1
    aritmetica1 = Aritmetica(2,4)
    aritmetica1.sumar()
    # Objeto 2
    aritmetica2 = Aritmetica(10,3)
    aritmetica2.resta()
    # Objeto 3
    #Otra forma de asignar valor a los paremetros es (se dejaron los valores como opcinales en el constructor de la clase):
    aritmetica3 = Aritmetica(55)
    aritmetica3.operando2 = 45
    aritmetica3.resta()
    #Objeto 4
    #Otra forma de definir parametros:
    aritmetica4 = Aritmetica(operando1=8, operando2=9)
    aritmetica4.sumar()