def mifuncion2 (argumento = 'chanchito'):
    print(argumento)

mifuncion2('Batman')
mifuncion2()

print('--------------------------------')

def mifuncionLista(lista):
    for el in lista:
        print(el)
    
mifuncionLista(['Chanchito', 'Feliz'])

print('--------------------------------')

def concatenarNombres(lista):
    i = ''
    for el in lista:
        i = i + ' ' + el
    return i

nombres = concatenarNombres(['Chanchito', 'Feliz'])
print(nombres)