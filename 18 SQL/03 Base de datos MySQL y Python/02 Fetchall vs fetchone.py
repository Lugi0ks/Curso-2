# tenemos 2 alternativas para mostrar las instacias de la bd
# fetchall lo que hará será devolver todas las instancias de los elementos que encontró en la base de datos y se los asignará a la variable que nosotros hemos declarado.

#fetchone Como podrán ver, esto es lo que hará será devolver solamente el primer elemento que éste ha encontrado por lo que si nosotros vamos a querer, por ejemplo en este caso que estamos buscando, todos los usuarios
# queremos, todos los usuarios tenemos que utilizar fetchone

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
resultado2 = cursor.fetchone()

print(resultado)
print(resultado2)

