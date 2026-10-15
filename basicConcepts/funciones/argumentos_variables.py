# argumentos variables:

def superheroe(nombre, nombre_superheroe, *args):
    print(f'Superheroe: {nombre} - {nombre_superheroe} = {args}')
    for poder in args:
        print(f'\tSuperpoder: {poder}')

superheroe('Peter', 'Spiderman', 'Telaraña', 'Fuerza sobre humana')
superheroe('Bruce Banner', 'Hulk', 'Super fuerza', 'Inteligencia', 'regeneración')