#Actualizar registros desde python a mysql
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
sentencia_sql = 'DELETE FROM personas WHERE id=%s'
valor = (5,) #Es necesari pasar una tupla, y esta e suna tupla d eun solo valor.
cursor.execute(sentencia_sql, valor)
personas_db.commit()
print('Element en base datos eliminado...')

cursor.close()
personas_db.close()
