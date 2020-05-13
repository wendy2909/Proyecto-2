import random
import os 
import sys
from collections import deque

historial = deque ()

os.system('cls')
print ("=================================================")
print ("                 BIENVENIDO :) ")
print ("================================================= \n")
print ("Elige tu Respuesta: \n ")
lista = ["0.salir","3.Tijera","2.papel", "1.Piedra"]
print (lista [3])
print (lista [2])
print (lista [1])
print (lista [0])
opcion = int(input(" >"))
Hola = random.randint (0,2)
compu = lista[Hola]
tu = lista [opcion]
print ("Computadora:", compu)
print ("Humano:",tu)
tu = input ("Resultado:")

if tu == compu:
    print (f"\n EMPATE!, \n {tu}")
elif (compu == [3]):
    if (tu == [2]):
        print("Gana Computadora!")
elif (tu == [1]):
        print ("Gana Humano!")

if (compu == [2]):
    if (tu == [1]):
        print ("Gana Computadora!")
elif (tu == [3]):
        print ("Gana Humano!")

if (compu == [1]):
    if (tu == [3]):
        print ("Gana Computadora!")
elif (tu == [2]):
        print ("Gana Humano!")

os.system('cls')
lista.append ("1.Piedra")
lista.append ("2.papel")
lista.append ("3.Tijera")

print(f"Historial Actual {lista} ")
print ("***************************************************")

while len (lista)  > 0 :
    ultima_accion = lista.pop()

print (f'Accion mas Reciente: {ultima_accion}')
print (f'Historial Actual: {lista}')
print ("****************************************************")

