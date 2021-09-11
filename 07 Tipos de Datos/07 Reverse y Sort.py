# Dar Vuelta y Ordenar la lista

# Creamos una nueva lista (Puede ser Numerica o de Caracteres)
Mueble = ['Mesa', 'Repisa', 'Velador', 'Estante']
print(Mueble)

# Ahora usaremos el metodo '.reverse()' el cual esta enfocado en dar vuelta lista
Mueble.reverse()
print(Mueble)

# Hora queremos ormenar la lista con un valor int primero agremagos el archivo
#Mueble.append(4)
#print(Mueble)

# Veamos que pasa cuando intentamos ordenar la lista
# Mueble.sort() no se puede mesclar un string y un int para poder ordenar

# Como no se puede ordenar la lista teniendo un integer lo agregaremos como un string 
Mueble.append('4')
print(Mueble)

# Veamos como se ve la lista despues de ser ordenada
Mueble.sort()
print(Mueble)
# Dejandola en orden alfabetico 