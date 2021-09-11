# a los metodos les podemos crear clases para que ellos hagan algo con sus datos

class Usuario:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludo(self):
        print('Hola, mi nombre es ', self.nombre, self.apellido)

usuario1 = Usuario('Daniel', 'Diaz')
usuario2 = Usuario('Diego', 'Tobar')

usuario1.saludo()
usuario2.saludo()