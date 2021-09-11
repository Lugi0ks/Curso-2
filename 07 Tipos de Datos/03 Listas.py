#Lista Vacia
lista = [] #para definir una lista que este vacia se utiliza '[]'
print(lista)
#Lista LLena
lista = [1,2,3]
print(lista)

#Manupulacion de una Lista

#Cuando quieres realizar unaa copia de la lista se crea una variable nueva y se le da el valor 
#de esta con el comando '.copy()'
lista2 = lista.copy() 
print(lista2)

#Cuando agregamos el '.append()' estamos diciendo que vamos agregar valores a la lista.
#Cuando utilizar el appernd solo puedes agregar un elemento a la lista
lista.append(4)
print(lista)

print(lista,lista2, sep=' - ')

#Con el '.clear' nos encargamos de limpiar la lista 
lista.clear()
print(lista)


