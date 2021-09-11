# Escribir un a funcion que que reciba Nombre y Apellido y los vaya agregando
# a un archivo
# 

from os import close, write


def NombreApellido(nom,ape):
    x = open("14 Ejercicios\\Nombre y Apellido.txt",'a') 
    x.write(nom + ' ' + ape +'\n')
    x.close()



r ='r'

while r != 'no':
    no = input('Ingresa tú Nombre:')
    ap = input('Ingresa tú Apellido:')

    NombreApellido(no.capitalize(),ap.capitalize())

    r = input('Si no deseas seguir agregando nombres escribe "no": ')
    r.lower()