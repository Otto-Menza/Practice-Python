print('** Manejo de Excepcoiones **')

def dividir(numerador, denominador):
    #Podemos usar el bloque try
    try:
        #podemos crear un escepcion dentro del try.  Pero es necesario llamar la exception despues con un except linea 17
        if denominador == 0:
            raise Exception('El denominador = 0, Error')

        resultado = numerador/denominador
        print(f'Reultado de la divicion {numerador}/{denominador} = {resultado}')
    except ZeroDivisionError:
        print(f'Error: No se peude dividir entre 0')
    except TypeError:
        print(f'Error de tipo: Los operandos deben ser numericos')
    # procesar de forma generica todos los errores posibles
    except Exception as error:
        print(f'Ocurrio un error: {error}')
    #o usa rel bloque else en caso de que no exista NINGUN error:
    else:
        print('No ocurrio NINGUN error')

    # Existe el bloque finally. SIEMPRE se va a ejecutar
    finally:
        print('Terminamos de procesar la Excepción\n')

dividir(10,2)
dividir(10,0)
dividir(10,'0')