class Gato:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola soy un gato y mi sonido es el, ',self.onomatopeya)

class Perro:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola soy un Perro y mi sonido es el, ',self.onomatopeya)


gato = Gato('Don Gato','Maullido')
gato.saludo()

perro = Perro('Don Gato','Ladrido')
perro.saludo()

# Como podemos mejorar este codigo si lo analizamos nos damos cuenta que ambos 
# comparten el nombre y onomatopella entonces creamos esa como una class unica para los 2 casos 

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

# Ahora que lo tenemos aislado creamos las clases perro y gato que van a eredar 
# el nombre y la onomatopeya

class Perro(Animal):
    def saludo(self):
        print('Hola soy un Perro y mi sonido es el, ',self.onomatopeya, ' y mi nombre es ',self.nombre)

class Gato(Animal):
    def saludo(self):
        print('Hola soy un Gato y mi sonido es el, ',self.onomatopeya, ' y mi nombre es ',self.nombre)

gato = Gato('Don Perro','Maullido')
gato.saludo()

perro = Perro('Don Gato','Ladrido')
perro.saludo() 

# Ahora lo vamos a simplificar aun mas

class Animal:
    def __init__(self, nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya
    
    def saludo(self):
        print('Hola soy un',self.tipo,'y mi sonido es el,',self.onomatopeya,  'y mi nombre es',self.nombre)

class Perro(Animal):
    tipo = 'Perro'

class Gato(Animal):
    tipo = 'Gato'

gato = Gato('Gatuu','Maullido')
gato.saludo()

perro = Perro('Perruuu','Ladrido')
perro.saludo() 