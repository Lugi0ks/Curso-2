import math

print('------------------------------------------------------------------------')

def suma(numero1, numero2):
    print(numero1+numero2)

suma(2,3)
print('------------------------------------------------------------------------')

def suma(numero1, numero2):
    print(numero1+numero2)

x = suma(2,6)
print('------------------------------------------------------------------------')

#Uso de la clase math.ceil para aproximar el valor al entero superior mas cercano
def MaterialConFoco(MaterialSinFoco,TasaDebolucion):
    print(math.ceil(MaterialSinFoco*((100-TasaDebolucion)/100)))

d = MaterialConFoco(208,47)
print('------------------------------------------------------------------------')

#Uso de round para aproximar el valor al entero mas cercano
def MaterialConFoco(MaterialSinFoco,TasaDebolucion):
    print(round(MaterialSinFoco*((100-TasaDebolucion)/100)))

d = MaterialConFoco(208,47)
print('------------------------------------------------------------------------')

#Uso de round para aproximar el valor al entero inferior mas cercano
def MaterialConFoco(MaterialSinFoco,TasaDebolucion):
    print(math.floor(MaterialSinFoco*((100-TasaDebolucion)/100)))

d = MaterialConFoco(208,47)
print('------------------------------------------------------------------------')

# forma de hacer para que la funcion no imprima hasta que se le ordene
def suma(numero1, numero2):
    return numero1+numero2

f = suma(2,8)
print ("El resultaddo de la suma de n1 y n2 es:")
print(f)



