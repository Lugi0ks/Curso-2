# para conectarnos a sql instalaremos el conector mediante pip pip install mysql-connector-pyhthon
# y realizamos la conexion a la bd de la siguiente forma

from colorama import Cursor
import mysql.connector

midb=mysql.connector.connect(
        host='localhost',
        user='Lugi0k',
        password='w4t4m0t31!',
        database='prueba'
    )

cursor= midb.cursor()

cursor.execute('select * from cliente')

resultado = cursor.fetchall()

print(resultado)

