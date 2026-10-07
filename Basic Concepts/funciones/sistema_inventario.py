# Sistemas de inventario cpn funciones
inventario = [
    {
        'id':1,
        'nombre': 'Camisa',
        'precio': 20,
        'cantidad': 100
    },
    {
        'id':2,
        'nombre': 'Pantalon',
        'precio': 30,
        'cantidad': 50
    },
    {
        'id':3,
        'nombre': 'Gorra',
        'precio': 50,
        'cantidad': 20
    }
]

def mostrar_inventario():
    global inventario
    for producto in inventario:
        print(f'ID: {producto.get('id')} | Nombre: {producto.get('nombre')}, Precio: ${producto.get('precio')}, Canridad: {producto.get('cantidad')}')

def agregar_producto():
    print('Ingresa los datos del producto')
    id = int(input('ID: '))
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    cantidad = int(input('Cantidad: '))
    global inventario
    inventario.append({
        'id': id,
        'nombre': nombre,
        'precio': precio,
        'cantidad': cantidad
    })

def buscar_producto(id):
    producto_encontrado = False
    for producto in inventario:
        if producto.get('id') == id:
            print(f'ID: {producto.get('id')} | Nombre: {producto.get('nombre')}, Precio: ${producto.get('precio')}, Canridad: {producto.get('cantidad')}')
            producto_encontrado = True
            break
    if not producto_encontrado:
        print('Producto no encontrado')


salir = False
while not salir:
    print('''*** Menu ***
    1. Mostrar inventario
    2. Agregar nuevo producto
    3. Buscar producto or ID
    4. salir''')
    opcion = int(input('Ingresa la opción que quieres: '))
    if opcion == 1:
        mostrar_inventario()
    elif opcion == 2:
        agregar_producto()
    elif opcion == 3:
        id = int(input('Ingresa el id a buscar: '))
        buscar_producto(id)
    elif opcion == 4:
        print('Slaiendo del sistema....')
        salir = True
    else:
        print('Opción invalida,intenta de nuevo')