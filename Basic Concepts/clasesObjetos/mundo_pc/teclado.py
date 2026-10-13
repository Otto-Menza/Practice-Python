from dispositivo_entrada import DispositivoEntrada

#Clase de teclado:
class Teclado(DispositivoEntrada):
    contador_teclado = 0
    #definir constructor o inicializafdpr
    def __init__(self, marca, tipo_entrada):
        Teclado.contador_teclado += 1
        self.id_teclado = Teclado.contador_teclado
        super().__init__(marca, tipo_entrada)

    def __str__(self):
        return (f'Teclado # {self.id_teclado} - Marca: {self.marca} - Tipo: {self.tipo_entrada}')

if __name__ == '__main__':
    teclado1 = Teclado('gamer', 'USB')
    print(teclado1)