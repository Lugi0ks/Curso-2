# La herencia es un concepto que se utiliza en la programacion de objetos para 
# poder reutilizar lo maximo posible un codigo con una estructura igual
class Usuario:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludo(ponny):
        print('Hola, mi nombre es ', ponny.nombre, ponny.apellido)

class Admin(Usuario):
    def superSaludo(self):
        print('Hola me llamo ',self.nombre, ' y soy admin')

admin = Admin('Julio', 'Diaz')

admin.saludo()
print('Para este caso se utilizo como referencia el Saludo que estoy heredando de la otra clase')
print('-----------------------------------')
admin.superSaludo()
print("Paara este caso estoy utilizando el saludo de mi propia clase")