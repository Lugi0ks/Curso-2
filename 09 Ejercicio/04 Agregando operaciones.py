n1 = input('Ingresa el primer Valor: ')
try:
    n1 = int(n1)
except:
    n1 = 'No es un valor numerico'

if n1 == 'No es un valor numerico':
    print('El Valor no es valido')
    exit()

n2 = input('Ingrese el segundo Valor: ')
try:
    n2 = int(n2)
except:
    n2 = 'No es un valor numerico'

if n1 == 'No es un valor numerico':
    print('El Valor no es valido')
    exit()

simbolo = input('Ingrese Operecion: ')
if simbolo == '+':
    print(n1 + n2)
elif simbolo == '-':
    print(n1 - n2)
elif simbolo == '*':
    print(n1 * n2)
elif simbolo == '/':
    print(n1 / n2)
