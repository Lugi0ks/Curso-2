# Para instalar camelcase vamos a usar el comando 'pip' luego la palabra 
# 'install' y para finalizar el paquete que queramos instalar en este caso 
# 'camelcase' en la terminal de está manera "pip install camelcase" 
# reinicias el editor de texto y listo

# Cuando se instale te aparesera lo siguente 
''''
Collecting camelcase
  Downloading camelcase-0.2.tar.gz (1.3 kB)
Using legacy 'setup.py install' for camelcase, since package 'wheel' is not installed.
Installing collected packages: camelcase
    Running setup.py install for camelcase ... done
Successfully installed camelcase-0.2
WARNING: You are using pip version 21.1.3; however, version 21.2.4 is available.
You should consider upgrading via the 'C:\x\x\x\x\x\x\x\python.exe -m pip install --upgrade pip' command.
'''
# Si quieres ver que paquetes tienes instalado usa el comando "pip list" en la consola
'''
PS C:\x\x\Python\Curso 2\12 Módulos> pip list
Package   Version
--------- -------
camelcase 0.2
WARNING: You are using pip version 21.1.3; however, version 21.2.4 is available.
You should consider upgrading via the 'C:\x\x\x\x\x\x\x\python.exe -m pip install --upgrade pip' command.
'''

# Ahora probaremos como funciona el paquete camelcase
# Primero importamos el paquete dandole el nombre CamelCase
'''
from camelcase import CamelCase
c = CamelCase()
s = 'Esta oración necesita CamelCasteada'
print (c.hump(s))
'''
# Para eliminar un paquete se utiliza el comando 'uninstal' donde va el install 
# pip uninstal camelcase te pregunta si deseas eliminar le das a 'y' y ya esta desinstalado
