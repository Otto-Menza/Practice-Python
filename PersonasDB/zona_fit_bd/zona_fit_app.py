from zona_fit_bd.cliente import Cliente
from zona_fit_bd.cliente_dao import ClienteDAO

print('** CLientes de zona fit ***')
opcion = None
while opcion != 5:
    print(f'''Menu:
    1. Listar clientes
    2. Aguregar cliente
    3. Modificar cliente
    4. Eliminar cliente
    5. Salir''')
    opcion = int(input('Ingeresa una opcion (1-5): '))
    if opcion == 1:
        clientes = ClienteDAO.seleccionar()
        print('\n*** Listado de Clientes ***')
        for cliente in clientes:
            print(cliente)
    if opcion == 2:
        nombre_cliente = input('Nombre de cliente: ')
        apellido_cliente = input('Apellido de cliente: ')
        membresia_cliente = input('Membresia de cliente: ')
        nuevo_cliente = Cliente(nombre=nombre_cliente, apellido=apellido_cliente, membresia=membresia_cliente)
        clientes_insertados = ClienteDAO.insertar(nuevo_cliente)
        print(f'\n Nuevo cliente ingeresado: {nuevo_cliente}')
    if opcion == 3:
        id_cliente = int(input('Ingresa ID del cliente a modificar: '))
        nombre_cliente = input('Nombre de cliente: ')
        apellido_cliente = input('Apellido de cliente: ')
        membresia_cliente = input('Membresia de cliente: ')
        cliente_actualizar = Cliente(id_cliente, nombre_cliente, apellido_cliente, membresia_cliente)
        clientes_actualizados = ClienteDAO.actualizar(cliente_actualizar)
        print(f'Clientes actualizados: {clientes_actualizados}')
    if opcion == 4:
        id_eliminar = int(input('Ingresa ID del cliente a eliminar: '))
        cliente_eliminar = Cliente(id=id_eliminar)
        clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
        print(f'Clientes eliminados: {clientes_eliminados}')
else:
    print('Saliendo de la app ...')
