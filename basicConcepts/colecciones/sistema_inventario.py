# Sistema de invetario:
#Primero definir la lista y la camtidad de diccionariosproductos que tendra.
invetario = []
cantidad_productos = int(input('¿Cuantos productos vas a ingresar?: '))

#Pedir los productos.
for i in range(cantidad_productos):
    invetario.append({
        'id':i+1,
        'nombre':input(f'Ingresa nombre del producto {i+1}: '),
        'precio':float(input('Ingresa el precio: ')),
        'cantidad':int(input('Ingresa la cantidad: '))
    })
print(invetario)

producto_encontrado = None
while producto_encontrado == None:
    id_buscar_producto = int(input('Ingresa el ID del producto a buscar: '))
    for producto in invetario:
        if producto.get('id') == id_buscar_producto:
            producto_encontrado = producto
            break

if producto_encontrado is not None:
    print(f'''Información del producto encontrado:
    ID: {id_buscar_producto}
        Nombre: {invetario[id_buscar_producto-1].get('nombre')}
        Precio: {invetario[id_buscar_producto-1].get('precio')}
        Cantidad: {invetario[id_buscar_producto-1].get('cantidad')}
    ''')

print('--- Invetario detallado actualizado ---')
for contador, producto in enumerate(invetario):
    print(f'''ID: {producto.get('id')}
    Nombre: {producto.get('nombre')}
    Precio: {producto.get('precio')}
    Cantidad: {producto.get('cantidad')}
    ''')