from zona_fit_bd.conexion import Conexion
from zona_fit_bd.cliente import Cliente


class ClienteDAO:
    SELECCIONAR = 'SELECT * FROM  cliente ORDER BY id'
    INSERTAR = 'INSERT INTO cliente(nombre, apellido, membresia) VALUES(%s, %s, %s)'
    ACTUALZIAR = 'UPDATE cliente SET nombre=%s, apellido=%s, membresia=%s WHERE id=%s'
    ELIMINAR = 'DELETE FROM cliente WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexio()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()
            #Mapeo de clase-tabla cliente
            clientes = []
            for registro in registros:
                cliente = Cliente(registro[0], registro[1], registro[2], registro[3])
                clientes.append(cliente)
            return clientes

        except Exception as e:
            print(f'Ocurrio error al seleciconar clientes: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def insertar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexio()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente.membresia)
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()
            return  cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al insertar cliente: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def actualizar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexio()
            cursor = conexion.cursor()
            valores = (cliente.nombre, cliente.apellido, cliente. membresia, cliente.id)
            cursor.execute(cls.ACTUALZIAR, valores)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio error al actualizar: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

    @classmethod
    def eliminar(cls, cliente):
        conexion = None
        try:
            conexion = Conexion.obtener_conexio()
            cursor = conexion.cursor()
            valor = (cliente.id,)
            cursor.execute(cls.ELIMINAR, valor)
            conexion.commit()
            return cursor.rowcount
        except Exception as e:
            print(f'Ocurrio un error al eliminar: {e}')
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)

if __name__ == '__main__':
    #Eliminar cliente
    cliente_eliminar = Cliente(3)
    clientes_eliminados = ClienteDAO.eliminar(cliente_eliminar)
    print(f'CLientes eliminados: {clientes_eliminados}')


    #Actualizar clientes
    # cliente_actualizar = Cliente(nombre='Alejandra', apellido='Torres', membresia=300, id=3)
    # cliente_actualizado = ClienteDAO.actualizar(cliente_actualizado)
    # print(f'Cliente actualizado: {cliente_actualizado}')

    #Insertar clientes
    # cliente1 = Cliente(nombre='Alejandro', apellido='Tellez', membresia=300)
    # clientes_insertados = ClienteDAO.insertar(cliente1)
    # print(f'Clientes insertados: {clientes_insertados}')

    #Seleccionar clientes
    clientes = ClienteDAO.seleccionar()
    for cliente in clientes:
        print(cliente)