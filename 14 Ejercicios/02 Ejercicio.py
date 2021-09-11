# Ingresar Nombre y Apellido e imprimir al reves 
def impresion(nombre, apellido):
    print(apellido, nombre)

n = input('Ingrese su Nombre: ')
a = input('Ingrese su Apellido: ')

impresion(n,a)


nombre = 'Diego'
apellido = 'Tobar'

concadenacion = nombre + ' '+ apellido
print(concadenacion[::-1])