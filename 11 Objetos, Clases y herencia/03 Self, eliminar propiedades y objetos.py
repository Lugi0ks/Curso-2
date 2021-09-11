# No es necesario que la palabra 'self' sea esta tambien puede ser ponny ejemplo

print('Ejemplo de cambiar la palabra "self" por "ponny" en el codigo en la variable de saludo')

class Usuario:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludo(ponny):
        print('Hola, mi nombre es ', ponny.nombre, ponny.apellido)

usuario1 = Usuario('Daniel', 'Diaz')
usuario2 = Usuario('Diego', 'Tobar')

usuario1.saludo()
usuario2.saludo()

print('------------------------------------------')

# Supongamos que ya no queremos que el usurio1 se llame daniel sino 
# julio para esto vamos a hacer lo siguiente

usuario1 = Usuario('Daniel', 'Diaz')
usuario1.saludo()
# Vemos que es daniel el nombre del usuario1
usuario1.nombre = 'Julio'
# Le cambiamos el valor del nombre a julio 
usuario1.saludo()
# Vemmos si quedo como queriamos

print('------------------------------------------')

# Para eliminar las propiedades de un usuario o un usuario se utiliza 
# la palabra reservada 'del'
print('Ejemplo de la eliminacion del usuario2')
del usuario2
print(usuario1.nombre)
# usuario1.saludo()
# print(usuario2)
# Esto nos dara un error de que el usuario2 no esta definido puesto que se elimino