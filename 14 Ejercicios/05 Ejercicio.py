# Escribir una funcion que indique si el usuario es mayor de edad

def mayorE(e):
    if e >= 18:
        print('Es Mayor de edad')
    else:
        print('Es Menor de edad')

g = int(input('Que edad tienes?: '))

d = mayorE(g)