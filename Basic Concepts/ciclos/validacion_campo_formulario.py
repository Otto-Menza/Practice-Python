#Validacion de campos
nombre_usuario = None
while not nombre_usuario or len(nombre_usuario)<2 or len(nombre_usuario)>10:
    nombre_usuario = input('Indica un nombre de usuario valido: ')
print(f'Nombre de usuario proporciondo es: {nombre_usuario}')