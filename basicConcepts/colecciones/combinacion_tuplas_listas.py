#Combinacion entre listas y tuplas. Ej: lista de productos

#Definir una lista de productos:
productos = [
    ('P001', 'Camisa', 30),
    ('P002', 'Pantalon', 25),
    ('P003', 'Gorro', 15)
]
precio_total = 0
print('Información de los productos:')
for producto in productos:
    id, nombre, precio = producto
    print(f'Producto id: {id}, Nombre: {nombre}, Precio: ${precio}')
    precio_total += precio
print(f'Precio Total de productos: {precio_total}')