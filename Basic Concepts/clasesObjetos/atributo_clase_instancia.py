# atributos de clase
class Persona:
    atributo_clase = 0
    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia

if __name__ == '__main__':
    print(f'--- Atributos de Clase ---')
    print(f'Este es el atributo de clase: {Persona.atributo_clase}')

    #Mpdificar el atributp de Clase
    Persona.atributo_clase = 10
    print(f'Este es el nuevo valor de atributo de clase: {Persona.atributo_clase}')

    #creamos 2 opbjetos y modificamos su atributo, pero veremos que el atributo de clase es el mismo.
    persona1 = Persona(5)
    print(f'Atributo de clase desde persona1 = {persona1.atributo_clase}') #Se puede llamr el atributo de clase desde el objeto, pero no e slo recomendado
    print(f'Atributo de instancia desde persona1 = {persona1.atributo_instancia}')
    ## otro objeto
    persona2 = Persona(8)
    print(f'Atributo de clase desde persona2 = {persona2.atributo_clase}')  # Se puede llamr el atributo de clase desde el objeto, pero no e slo recomendado
    print(f'Atributo de instancia desde persona2 = {persona2.atributo_instancia}')