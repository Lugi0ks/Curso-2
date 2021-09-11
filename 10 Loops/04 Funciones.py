# Son bloques de codigo que no se ejecuntan al menos que sean llamadas, ademas 
# se utilizan como para reutilizar codigo para no tener que hacerlo nuevamente

def miFuncion():
    print('Mi Primera Función')

miFuncion()

print('-----------------------------------------------')

def imprimeDato(argumento):
    print('Mi argumento es,',argumento)

imprimeDato('parametro 1')

print('-----------------------------------------------')

def suma(numero1, numero2):
    print(numero1+numero2)

suma(2,3)

print('-----------------------------------------------')

'''

Cuando una funcion tiene mas de una entrada y en esta sole le 
ingresan 1 esta te dara un error puesto que ella esta pidiendo 2 y no una

def formulario(nombre, apellido):
    print('El Nombre completo es, ',nombre ,apellido)

formulario('Juan')

'''
# Por otra parte si quiero colocar 2 valores y en la funcion tengo definido 
# que este es 1 tambien dara el error almenos que le coloquemos el simbolo de 
# '*' antes del nombre de la variable asi este entrara como una suerte de lista
def formulario(*nombre):
    print('El Nombre completo es, ',nombre)

formulario('chanchito','Feliz','Lala','Lele')

print('-----------------------------------------------')

def NombreCompleto(apellido, nombre):
    print(nombre,apellido)

NombreCompleto(nombre='Chanchito', apellido='Feliz')

print('-----------------------------------------------')

def NombreCompleto2(**kwargs):
    print(kwargs['nombre'],kwargs['apellido'])

NombreCompleto2(nombre='Chanchito', apellido='Feliz')