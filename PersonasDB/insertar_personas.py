#insertar registros desde python a mysql
import mysql.connector
#Crear objeto para conectarse a la base
personas_db = mysql.connector.connect(
    host='localhost', #o la IP local: 127.0.0.1
    user='root',
    password='Admin123*',
    database='personas_sb'
)

#Ejecutar la sentencia SELECT
cursor = personas_db.cursor()
sentencia_sql = 'INSERT INTO personas(nombre, apellido, edad) VALUES(%s, %s, %s)'
valores = ('Jose', 'Gonzalez', 75)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print(f'Se ha agregado los nuevos registros a la base de datos: {valores}')


#Cerrar los objetos que llamaos:
cursor.close()
personas_db.close()