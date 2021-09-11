# Escribe una funcion que nos permita saber si el numero es par o impar
def NumParIMpar(num):
    if num % 2 == 0 :
        print("El Numero es Par")
    else:
        print("El Numero es Impar")

c = int(input('Ingresa el Numero que quieras saber si es par o impar:'))

NumParIMpar(c)