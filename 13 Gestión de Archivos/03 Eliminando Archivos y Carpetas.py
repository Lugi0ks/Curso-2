# Para eliminar un archivo o carpeta tendremos que importar una  libreria llamada 'os' 
import os 

# os.remove('C:\\Users\\Lugi0ks\\Python\\Curso 2\\13 Gestión de Archivos\\Test.txt')

# Si usamos esta sentencia nuevamente nos dara un error puesto que el archivo ya no existe para esto 
# lo validaremos

if os.path.exists('C:\\Users\\Lugi0ks\\Python\\Curso 2\\13 Gestión de Archivos\\Test.txt'):
    os.remove('C:\\Users\\Lugi0ks\\Python\\Curso 2\\13 Gestión de Archivos\\Test.txt')
else:
    print('El archivo no existe')


# Ahora para borrar Una carpeta Usamos el rmdir y lo validamos para que no de problemas

if os.path.exists('C:\\Users\\Lugi0ks\\Python\\Curso 2\\13 Gestión de Archivos\\Test.txt'):
    os.rmdir('C:\\Users\\Lugi0ks\\Python\\Curso 2\\13 Gestión de Archivos\\Test.txt')
else:
    print("La Carpeta no Existe")