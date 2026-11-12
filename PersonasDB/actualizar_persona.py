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
sentencia_sql = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s'
valores = ('Victoria', 'Peres', 54, 4)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('Se han actualizado los datos...')

cursor.close()
personas_db.close()
