# Escribe una fincion que indique cuantas vocales tiene una palabra

def ContVocales(pal):
    cant= 0
    for x in pal:
        if x=='a' or x=='e' or x=='i' or x=='o' or x=='u' or x=='A' or x=='E' or x=='I' or x=='O' or x=='U':
            cant= cant+1
    print('El total de las vocales en la palabra son: ',cant)

p = input('Ingresa la palabra para contar sus vocales:')

ContVocales(p)