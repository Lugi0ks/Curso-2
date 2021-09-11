# agregando datos con el metodo append

x = open("C:\\Users\\Lugi0ks\\Python\\Curso 2\\13 Gestión de Archivos\\Test.txt",'a')

x.write(" alersis")

# si revisamos el archivo nos agrego la frace  despues de la siguiente 
# pero que pasa si yo quiero que esta este en una nueva linea le agregamos
# /n 
# 

x.write("\nalexis") 

x.close()
# ---------------------------------------------------------------------------------------

c = open("C:\\Users\\Lugi0ks\\Python\\Curso 2\\13 Gestión de Archivos\\Test.txt")

print(c.read())

c.close()

# ---------------------------------------------------------------------------------------

# Ahora veremos el comportamiento que tiene la opcion 'w' al momento de manipular el archivo
x = open("C:\\Users\\Lugi0ks\\Python\\Curso 2\\13 Gestión de Archivos\\Test.txt","w")
x.write("Este es el Metodo Write para el archivo Test.txt")

x.close()

c = open("C:\\Users\\Lugi0ks\\Python\\Curso 2\\13 Gestión de Archivos\\Test.txt")

print(c.read())

c.close()

# Como vemos con este metodo nos re-escrivio el archivo con la ultima frase que nosotros 
# le agregamos  