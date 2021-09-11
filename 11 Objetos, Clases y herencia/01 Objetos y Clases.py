# Planos reprecenta las clases
# Casas las clases contruidas a los objetos

class Usuario:
    nombre = "Julio"
    apellido = "Díaz"

usuario = Usuario()

print(usuario)
# al imprimir esto me da  <__main__.Usuario object at 0x000002300999C2E0>
print("------------------------------")
# para ver lo que contenga la clase se realiza de la siguiente forma
print(usuario.nombre)
print("------------------------------")
print(usuario.nombre, usuario.apellido)
print("------------------------------")

# Para cuando se tenga que crear mas de un usuario con distintos nombres y apellidos
# al momento de crear una instancia y se realiza de la siguiente manera

class Usuario2:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

usuario1 = Usuario2('Daniel', 'Diaz')
usuario2 = Usuario2('Diego', 'Tobar')

print(usuario1.nombre, usuario1.apellido, usuario2.nombre, usuario2.apellido)
# self permite al usuario especificar y acceder a los atributos y métodos de una 
# instancia de la clase