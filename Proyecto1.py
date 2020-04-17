import os
import sys
os.system ('cls')
valido = input ('---------- Su Carpeta es: ---------- \n')
valido = input (os.path.isdir('Proyecto_Darsy_Wendy'))
valido = input ('Presione una Tecla Para Continuar......')

os.system ('cls')
valido = input ('Los Archivos que Contienen Su Carpeta Son:  \n')
valido = input ( 'Nombres Originales:')
valido = input (os.listdir('Proyecto_Darsy_Wendy'))
valido = input ('Presione una Tecla para Continuar....\n')

os.system ('cls')
Nuevo = input ('Nombres Nuevos:')
Nuevo = input ('Ejemplo1.jpg')
Nuevo = input ('Ejemplo2.jpg')
Nuevo = input ('Ejemplo3.jpg')