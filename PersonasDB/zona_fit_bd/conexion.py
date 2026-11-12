from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE = 'zona_fit_bd'
    USERNAME = 'root'
    PASSWORD = 'Admin123*'
    DB_PORT = '3306'
    HOST = 'localhost'
    POOL_SIZE = 5
    POOL_NAME = 'zona_fit_pool'
    pool = None

    @classmethod
    def obtener_pool(cls):
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name=cls.POOL_NAME,
                    pool_size=cls.POOL_SIZE,
                    host=cls.HOST,
                    port=cls.DB_PORT,
                    database=cls.DATABASE,
                    user=cls.USERNAME,
                    password=cls.PASSWORD
                )
                return cls.pool
            except Error as e:
                print(f'Ocurrio un error al obtener pool: {e}')
        else:
            return cls.pool

    @classmethod
    def obtener_conexio(cls):
        return cls.obtener_pool().get_connection() #Del objeto de tio pool ahora sacamos un objeto de tipo conexion.

    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close() #cerramos la conexcion, se libera la conexion.

if __name__ == '__main__':
    #creamos un pbjeto pool
    pool = Conexion.obtener_pool()
    print(pool)
    conexion1 = pool.get_connection()
    print(conexion1)
    Conexion.liberar_conexion(conexion1)