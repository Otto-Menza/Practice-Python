from dispositivo_entrada import DispositivoEntrada

#clase de Raton
class Raton(DispositivoEntrada):
    contador_raton = 0
    #defiir constructor / inicialziar la clase:
    def __init__(self, marca, tipo_entrada):
        Raton.contador_raton += 1
        self.id_raton = Raton.contador_raton
        #self.marca = marca #una forma de inicializar
        #self.tipo_entrada = tipo_entrada
        #tambien se eud einicializar llamando el metodo que ya existe en la clase padre:
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return (f'Entrada # {self.id_raton} Marca: {self.marca} Tipo: {self.tipo_entrada}')

if __name__ == '__main__':
    raton1 = Raton('hp', 'USB')
    print(raton1)

