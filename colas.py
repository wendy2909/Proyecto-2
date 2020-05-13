import os
import sys
from collections import deque
Archivo = deque()

os.system('cls')
print ("=================================================")
print ("                 BIENVENIDO :) ")
print ("================================================= \n")
print ("Desea?\n ")
print ("1. Agregar un elemento a la cola de impresion")
print ("2. Imprimir")
print ("3. Salir\n")
opcion = int(input("Selecciona una opcion:"))
os.system('cls')
if opcion == 1:
    print ("Se encontraron los siguientes Archivos en la Carpeta Actual:\n ")
    datos = []   
    os.system('cls')
    valido = input('Los Archivos que contiene su carpeta son: ')
    valido = input(os.listdir('C:\\Users\\Darsy\\Desktop\\Archivos'))
    valido = input('Precione una tecla para continuar')
    lista = ["[1] Archivo1.txt","[2] Archivo2.txt","[0] Cancelar"]
    print (lista [0])
    print (lista [1])
    print (lista [2])
    print ("\n")
    print("Ingrese el numero de Archivo que desea agregar a la cola: \n")
    op = input()
    if op == "1":
        Archivo.append ("[1] Archivo1.txt")
    elif op == "2":
        Archivo.append ("[2] Archivo2.txt")
    elif op == "3":
        Archivo.append ("[3] Cancelar")
    print (f"La Cola de Impresion es: \n {Archivo}")
    print ("===================================================") 
elif opcion == 2:
    documento = Archivo.popleft()
    print(f"Documento impreso: {documento}")
    print(f"Cola de impresion:  {Archivo}")
    if len(Archivo) == 0:
        print("La cola esta vacia")
elif opcion ==3: 
    print("Gracias")
    sys.exit()
else: 
    print( "Ingrese opcion Valida")
