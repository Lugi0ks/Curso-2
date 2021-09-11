diccionario = {
    "Nombre" : "Red",
    "Raza" : "Persa",
    "Edad" : 2
}
print("Uso de '.pop()'")
# Ahora vamos a agregar valores a este diccionario
diccionario['Ronronea'] = 'Si'
print(diccionario)

#para Eliminar un valor usaremos el metodo ".pop()" donde en los parentecis\
#va el elemento a eliminar
diccionario.pop('Ronronea')
print(diccionario)

# Otra manera de eliminar el Ronronea ees usando ".popitem()" este nos eliminara el ultimo valor ingresado
diccionario['Ronronea'] = 'Si'
print("Uso de '.popitem()'")
print(diccionario)
diccionario.popitem()
print(diccionario)

# Otra forma de eliminar elementos del diccionario es usando la palabra 'del'
diccionario['Ronronea'] = 'Si'
print('Uso de "del"')
print(diccionario)
del diccionario['Ronronea']
print(diccionario)

# Ahora vamos hacer una copia de esta lista y le vamos a eliminar un valor
diccionario['Ronronea'] = 'Si'
nuevogato = diccionario.copy()
del diccionario['Ronronea']
print(diccionario, nuevogato ,sep=' - ')

# Para eliminar todos los datos del diccionario vamos a utilizar el metodo 
#'.clear()'
diccionario.clear()
print(diccionario, nuevogato, sep='-')

# Otra manera de realizar una copia vamos a utilizar el metrodo 'dict()'
diccionario = {
    "Nombre" : "Red",
    "Raza" : "Persa",
    "Edad" : 2
}
diccionario['Ronronea'] = 'Si'
diccionario2 = dict(diccionario)
print('Copia del diccionario utilizando "dict()"')
print(diccionario2)