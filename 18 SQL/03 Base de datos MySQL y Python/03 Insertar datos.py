from colorama import Cursor
import mysql.connector

midb=mysql.connector.connect(
        host='localhost',
        user='Lugi0k',
        password='w4t4m0t31!',
        database='prueba'
    )

cursor= midb.cursor()

''' 
para poder ir ingresando datos a la base de datos vamos a hacer algo distinto 

primero escribimos la consulta que usaremos si no recuerdas que modelo tiene tu bd usa una instrruccion para ver como esta esta con show create table (tabla)


cursor.execute('show create table Cliente')
 
resultado=cursor.fetchall()

print(resultado)


Como vemos nos muestra el formato de la tabla a insertar datos o lo que vallamos a realizar 

'Cliente', 
'CREATE TABLE `cliente` (
    `id` int NOT NULL AUTO_INCREMENT,
    `UserName` varchar(50) DEFAULT NULL,
    `email` varchar(50) DEFAULT NULL,
    `edad` int DEFAULT NULL,
    PRIMARY KEY (`id`)
    ) 
    
'''

'''
cuando nosotros vamos a ejecutar una consulta de SQL y además vamos a tener valores que vamos a querer que estos sean reemplazados después.

En ese caso, mi método de execute va a recibir dos argumentos el primero es la consulta SQL y el segundo argumento van a ser los valores que yo voy a ingresar luego de eso ya podemos ejecutar.

Sin embargo, los datos no van a quedar guardados en la base de datos hasta que nosotros no comprometamosestos cambios y para nosotros comprometer estos datos que nosotros queremos crear tenemos que llamar aquí a nuestra base de datos y seguido de Comit.

El método del Comit lo que hará será tomar estos datos y ejecutará la consulta SQL directamente contra la base de datos.

Seguido de esto, nosotros ahora vamos a poder llamar a lo siguiente cursor.rowcount

'''
sql = 'insert into cliente(UserName, email, edad)values(%s, %s, %s)'
values = ('python', 'inserto.con.python@mail.com', 41)

cursor.execute(sql, values)

midb.commit()

print(cursor.rowcount)

cursor.execute('select * from Cliente')
resultado = cursor.fetchall()
print(resultado)
'''
 [(1, 'rat', 'prueba.mail@mail.com', 24),
  (2, 'TheBigRat', 'TheBigRat@mail.com', 25), 
  (4, 'lugi0k', 'lugi0k@mail.com', 26), 
  (6, 'python', 'inserto.con.python@mail.com', 41)]
'''