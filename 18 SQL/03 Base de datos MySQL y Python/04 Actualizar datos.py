



import mysql.connector

midb=mysql.connector.connect(
        host='localhost',
        user='Lugi0k',
        password='w4t4m0t31!',
        database='prueba'
    )

cursor= midb.cursor()



sql = 'update Cliente set email = %s where id = %s '
values = ('lugiok@mail.com',4)
cursor.execute(sql,values)

midb.commit()
print(cursor.rowcount)