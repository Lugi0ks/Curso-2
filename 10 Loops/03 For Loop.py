# Se Utiliza para iterar sobrre listas o tuplas pero por lo general sobre una secuencia de datos 

#creamos una lista
Usuarios = ['Julio',"Roberto", 'Alexis']

# Donde el 'usuario' es el elemento voy a trabajar en este loop
# Que es lo que vamos a hacer vamos a imprimir los elementos 'usuarios'
# (a esta se le puede denominar de cualquier manera) que 
# se encuentran en la lista 'Usuarios' 

for usuario in Usuarios:
    print(usuario)

# Esto que ventaja nos da primero que no necetamos que calcular la cantidad de 
# elementos que esta lista tenia para luego ir viendo que es lo que contiene 
# por el uso del indice viendolos en total
print ('---------------------------------------')
# Tambien podemos iterar en strings como le mostraremos acontinuacion
NuevoUseuaro = 'Julio'

for x in NuevoUseuaro:
    print(x)

# En este caso nos imprimira cada uno de los caracteres que se encuentre en el sting
print('---------------------------------------')
# tambien se puede utilizar el camando 'break' en este tipo de loop

for x in Usuarios:
    if x == 'Roberto':
        break
    print(x)

# Cuando llega al nombre de Roberto este termina de ejecutar el loop
print('---------------------------------------')
# Tambien podemos utilizar el comando 'continue'

for y in Usuarios:
    if y == 'Roberto':
        continue
    print(y)

# Saltando al campo ya mencionado en este caso 'Roberto'
print('---------------------------------------')

# Ahora veremos el tipo de dato 'Range'

for r in range(6):
    print(r)

# Que es lo que pasa en este caso nos muestra un rango de 0 a 6 puesto que 6 
# es el tope para nuesto 'range' tambien podemos poner que inicie desde el 2 
# de la siguiente manera
print('---------------------------------------')

for r in range(2,6):
    print(r)

# Al poner el '2,6' da a entender que tiene que iniciar en el 2 para terminar en el 6
print('---------------------------------------')
# Tambien podemos ir aumentando la sumatoria hasta llegar al numero deseado 
# colocando una ',x' # donde la x es el valor creciente del la sumatoria

for r in range(2,30,4):
    print(r)

print('---------------------------------------')

# En el caso de terminar de utilizar el 'for' podremos utilizar el 'else' para mostrar 
# que se termino el loop

for r in range(2,30,4):
    print(r)
else:
    print('Termino el LOOP')

    