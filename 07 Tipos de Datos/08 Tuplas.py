# las tuplas y las listas son parecidas pero las diferencian que al momento de 
#crearlas ya no pueden ser modificadas al contrario de las listas 

# Para crear una tupla se crea la variable x y en vez de utilizar '[]' se utilizan
#() de tal modo que queda asi "x = ()"
varia = ('Hola', 'Mundo', 'somos', 'Tupla')
print(varia)

# Para estos tipos de variables se pueden complementar con '.count()', '.index()'
print(varia.count('Hola'))
print(varia.index('Mundo'))

# Para Modificar una Tupla Primero tenemos que transformarla a una Lista y se hace
#de la siguiente manera
ListaDeTupla = list(varia)
# Como se puede ver la variable 'ListaDeTupla' va a contener a la Tupla pero antes
#se formatea con el formato de lista y agregamos un valor a la lista
ListaDeTupla.append('A hora soy una Lista')
print(ListaDeTupla)

# Y viceversa podemos dejar una lista como una tupla utilizando la misma logica
Tupla = tuple(ListaDeTupla)
print(Tupla)