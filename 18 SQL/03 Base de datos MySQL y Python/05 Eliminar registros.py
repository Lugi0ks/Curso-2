

import mysql.connector

midb=mysql.connector.connect(
        host='localhost',
        user='Lugi0k',
        password='w4t4m0t31!',
        database='prueba'
    )

cursor= midb.cursor()


sql = 'delete from cliente where id = %s'
values= (6,)
cursor.execute(sql, values)
midb.commit()