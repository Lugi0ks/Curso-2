# Escribir una funcion que encuentre el elemento menor de una lista

lista = [1,2,5,7,8,23,-12]

menor = 'init'

for x in lista:
    if menor == 'init':
        menor = x
    else:
        menor = x if x < menor else menor

print('menor',menor)