# n1 = int(input('Ingrese el Primer Numero \n'))
# n2 = int(input('Ingrese el Segundo Numero \n'))
# r= n1+n2
# print(r)

n1 = input('Ingresa el primer Valor: ')
try:
    n1 = int(n1)
except:
    n1 = 'No es un valor numerico'

n2 = input('Ingrese el segundo Valor: ')
try:
    n2 = int(n2)
except:
    n2 = 'No es un valor numerico'

if n1 == 'No es un valor numerico' or n2 =='No es un valor numerico':
    print('Los valores ingresados no son numericos')
else:
    print(n1 + n2)