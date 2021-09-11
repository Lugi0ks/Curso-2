class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    
    def saludo(self):
        print('Hola soy un',self.tipo,', mi sonido es el,',self.onomatopeya,  'y mi nombre es',self.nombre)

class Perro(Animal):
    tipo = 'Perro'
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self,nombre, onomatopeya)
        print('Hola Soy un perro extendido')

class Gato(Animal):
    tipo = 'Gato'
    def __init__(self, nombre, onomatopeya):
        super().__init__(nombre, onomatopeya)
        print("Soy un Gato Extendido")

gato = Gato('Gatuu','Maullido')
gato.saludo()

perro = Perro('Perruuu','Ladrido')
perro.saludo() 