#Usaremos el While anterior

# Ahora que es lo que pasaria si queremos detener la ejecucion de este 
# ciclo cuando se cumpla una condicion para esto vamos a utilizar la palabra 
# 'break' dentro de la condicion la condicion

i = 0

'''
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1
'''

# Ahora si queremos que cuando llegue a la condicion salte directamente 
# al while nuevamente usaremos el 'continue' esto trae un problema si dejamos 
# que este sea 3 nos hara un ciclo infinito si mantenemos ese orden y para 
# solucionarlo cambiaremos la posicion del print y la suma del valor 

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    
