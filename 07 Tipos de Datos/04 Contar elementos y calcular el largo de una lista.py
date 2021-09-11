# Esto se puede usar con el elemento '.count(x)' donde x es el elemento a contar Ejemplo
lista = [1,2,3,4]
print('Buscando Cuantos 5 existen en la lista')
print(lista.count(5))
# En este caso no se encontro el numero 5 dandonos el valor de 0 en pantalla ahora veamos
#cuantos 3 tiene la lista
print('Buscando cuntos 3 tiene la lista')
print(lista.count(3))
# Para este caso nos mostrara que solo existe un tres dentro de esta

# Para ver cuantos elementos tiene la lista usaremos el elemento 'len(x)' donde x es
#la lista a contar (los elementos que esta contenga)
print('Contando cuantos elementos contiene la lista')
print(len(lista))
# Otra forma de poder ver el largo de una lista es creando una variable que esta contenga el largo de la lista a vert
LargoLista = len(lista)
print('Contando los elementos que tiene la lista utilizando una variable')
print(LargoLista)