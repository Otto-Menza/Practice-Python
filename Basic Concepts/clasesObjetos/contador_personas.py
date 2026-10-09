# Contadpr de personas
class Persona:
    # Atributo de la clase
    contador_persona = 0

    #constructor d ela clase:
    def __init__(self, nombre, apellido):
        # Incrementamos el valor del atributo de la clase
        Persona.contador_persona += 1
        self._id = Persona.contador_persona
        self._nombre = nombre
        self._apellido = apellido

    #definimos el metodo get y set d eforma pythonica
    @property #Metodo get
    def id(self):
        return self._id
    @id.setter #metodo set
    def id(self, id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombe(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido
    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    def mostar_persona(self):
        print(f'Persona: {self._id} - {self._nombre} {self._apellido}')

#Programa:
if __name__ == '__main__':
    print('** Ejemplo de contador de personas con contador en atributo de clase **')
    persona1 = Persona('Pedro', 'Gonzalez')
    persona2 = Persona('Angie', 'Vega')
    persona1.mostar_persona()
    persona2.mostar_persona()
    #Imprimir el valor de objetos de personas
    print(f'Cantidad de objetos: {Persona.contador_persona}')