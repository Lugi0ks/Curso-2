# Son parecidos a las listas pero con la diferencia de acceder a los elementos 
#de un diccionario en vez de usar numeros usaremos string

# Agregamos un diccionario
diccionario = {
    "Nombre" : "Red",
    "Raza" : "Persa",
    "Edad" : 2
}
print(diccionario)

# Para ver solo un valor del diccionario al momento de imprimir colocamos '[]' 
#y adentro de estos ponemos el campo a ver ejempo quiero ver solo el nombre 
#tendriamos que poner 'print(diccionario['Nombre'])'
print(diccionario['Nombre'])

# La otra forma de llamar solo a un elemento es utilizando el metodo '.get()'
print(diccionario.get('Edad'))

# Si quiero cambiar algun elemento del diccionario primero lo llamamos y 
#tilizamos el '[]' # y colocamos el campo a cambias luego usamos '=' 
#para asignarle el nuevo valor
# Cambiemos el Nombre al gato
diccionario['Nombre'] = 'Soul'
print(diccionario['Nombre'])

# Tambien podemos ver la cantidad de elementos que el diccionario tiene 
#utilizando el elemento len
print(len(diccionario))
