''' 
En algunas ocasiones, nosotros, cuando queramos solicitar información, no vamos a necesitar todos

los datos o vamos a querer limitarlos para que solamente nos devuelvan un set de datos en lugar del

total que se encuentran dentro de nuestra tabla.

Para eso nosotros podemos tomar esto mismo.

Voy a aprovechar de tomar ya, pero no voy a pegar.

Y aquí al final no tenemos que agregarle la palabra reservada de LIMIT.

Seguido de eso tenemos que indicar cuántos elementos nosotros queremos limitar y aquí nosotros lo vamos

a dejar en uno.

Esto es lo que hará será retornar solamente un elemento de lo que encuentre en toda su consulta.

Vuelvo a ejecutar mi script y aquí vemos ahora que me devolvió solamente un elemento en el caso que

yo indique.

2.

En ese caso me va a devolver dos elementos.
'''


import mysql.connector

midb=mysql.connector.connect(
        host='localhost',
        user='Lugi0k',
        password='w4t4m0t31!',
        database='prueba'
    )

cursor= midb.cursor()


cursor.execute('select * from cliente limit2')
resultado= cursor.fetchall()
print(resultado)