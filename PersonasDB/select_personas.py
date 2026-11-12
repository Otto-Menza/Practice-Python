#seleccionar registros desde python a mysql
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
cursor.execute('SELECT * FROM personas');
resultado = cursor.fetchall()
for persona in resultado:
    print(persona)


#Cerrar los objetos que llamaos:
cursor.close()
personas_db.close()