#Maquina de snaks
snaks = [
    {'id':1, 'nombre':'papas', 'precio':2000},
    {'id':2, 'nombre':'platanitos', 'precio':3000},
    {'id':3, 'nombre':'agua', 'precio':2500}
]
total = 0
ticket = []
#Funcion para mostrar los snaks
def mostrar_inventario():
    for producto in snaks:
        print(f'ID: {producto.get('id')} | Nombre: {producto.get('nombre')}, Precio: ${producto.get('precio')}')

#funcion para buscar snak, agregarlo al tiket y sumarlo al costo total
# def comprar_snak():
#     id_snak = int(input('Ingresa el id el producto: '))
#     for producto in snaks:
#         if producto.get('id') == id_snak:
#             producto_add_ticket = {'id':producto.get('id'), 'nombre':producto.get('nombre'), 'precio':producto.get('precio')}
#             ticket.append(producto_add_ticket)
#             print(f'Snack agregado = ID: {producto_add_ticket}')
#             global total
#             total += producto.get('precio')
#             return
#     print('Producto No encontrado...')

#Otra forma: insertando/creando funciones mas pequeñas para compartirla responsabilidad:
def buscar_snack_por_id(id_buscar):
    for snack in snaks:
        if snack.get('id') == id_buscar:
            return snack
    #Si llegamos al final y no se encontro el snack retornamos none
    return None
def comprar_snak():
    id_snack = int(input('Ingresa el id del snka a comprar: '))
    snack_encontrado = buscar_snack_por_id(id_snack)
    if snack_encontrado is not None:
        ticket.append(snack_encontrado)
        print(f'Snack Agregado: {snack_encontrado}')
    else:
        print(f'Snack No encontrado')

#Funcion para mostrar ticket
def total():
    total = 0
    for snack in ticket:
        total += snack.get('precio')
    return total
def mostrar_ticket():
    print('--- Ticket de venta ---')
    for producto in ticket:
        print(f' - {producto.get('nombre')}: ${producto.get('precio')}')
    print(f'TOTAL = ${total()}')

#Menu, confirmamos que solo se ejcute al ejecutar este archivo.
if __name__ == '__main__':
    while True:
        print('''*** Menu ***
            1. Mostrar Snacks
            2. Comprar Snacks
            3. Mostrar Ticket
            4. salir''')
        opcion = int(input('Ingresa la opción que quieres: '))
        if opcion == 1:
            mostrar_inventario()
        elif opcion == 2:
            comprar_snak()
        elif opcion == 3:
            mostrar_ticket()
        elif opcion == 4:
            print('Saliendo dle sistema...')
            break
        else:
            print('Opción invalida, intenta de nuevo')


