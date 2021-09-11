# escribe una aplicacion que reciba una cantidad infinita de números hasta 
# decir basta luego que devuelva la suma de los numeros ingresados
# 

suma = 0
 
while True:
    x = input('Ingresa tu valor: ').lower()
    if x == 'basta':
        print(suma)
        break
    else:
        try:
            x = int(x)
            suma += x
            continue
        except:
            x = 'error'
            print('Por favor ingresa un valor numerico')
            exit()