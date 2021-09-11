

# Recuerdan el archivo de Hola mundo? ahora vamos a generarlo como un txt con mas datos al
# interior de este ingresar a este mediante este archivo 

# Ahora vamos a contener el archivo en una variable y para esto 
# utilizaremos la funcion 'open' la cual se encarga de abrir los archivos 
# a esta se la asignamos a una variable para que contenga el archivo.

c = open("C:\\Users\\Lugi0ks\\Python\\Curso 2\\13 Gestión de Archivos\\Test.txt")

# Para leerlo utilizaremos el metodo 'read' para que nos lea la totalidad 
# del archivo

print(c.read())


# Ahora imaginemos que tenemos un monton de lineas esto nos dara un poco de 
# problemas al utilizar el comando 'read' 

# Veamos los permisos para los archivos que nos da pyton
# open('x') = Nos permite abrir un archivo en espesifico donde se encuentre este, 
#            ademas de esto esta recibe un segundo argumento 'x' que es un string 
#            el cual se trata del permiso que queramos darle:
#            'r'= de read permiso por defecto que es de leer el archivo
#            'a'= de append con este podemos modificar el archivo no en su 
#                 totalidad sino agregando al final de este lo que nosotros 
#                 desiemos
#            'w'= de write con este podremos modificar el archivo no solo agregando 
#                 al final de este, en el caso de que el archivo no exista este lo creara
#            'x'= con este caracter nos permite crear un archivo si este existe nos dara un error
# 
#    
# Que pasa si queremos leer de una linea para esto al 'read' le agregamos el 'line' quedando 
# readline()
# 
# Supongamos que queremos hacer esto pero de forma mas automatica usaremos el ciclo for para 
# automatizar el readline.
# 
for x in c:
    print(x)    
# 
# Siempre es buena practica cerrar el archivo con el metodo 'close()'
c.close() 
