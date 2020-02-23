#Primero y segundo programa

import time
from random import randint
#Leer archivo
f=open("mil.txt","r")
tiempo=time.time()
#Variable que hace la suma total
suma=0
#Contador
con=0
#Número aleatorio entre 1 y 4
numero=randint(1,4)
for x in f:
#If para si el número aleatorio coincide con alguno del archivo
#Int() convierte la x en un número entero para que pueda comparar
  if numero == int(x):
    #Si encuentra el contador cuenta uno y si encuentra mas #números
    con=con+1
  suma += int(x)
print("Mil datos")
print("Suma = "+str(suma))
print("Duracion "+str(time.time()-tiempo)+" segundos")
print("Número a validar: "+str(numero))
print("Número de veces q se repite en el archivo: "+str(con))
print("\n")


f=open("diezmil.txt","r")
tiempo2=time.time()
#Variable que hace la suma total
suma=0
#Contador
con=0
#Número aleatorio entre 1 y 4
numero=randint(1,4)
for x in f:
#If para si el número aleatorio coincide con alguno del archivo
#Int() convierte la x en un número entero para que pueda comparar
  if numero == int(x):
    #Si encuentra el contador cuenta uno y si encuentra mas #números
    con=con+1
  suma += int(x)
print("Diez mil datos")
print("Suma = "+str(suma))
print("Duracion "+str(time.time()-tiempo2)+" segundos")
print("Número a validar "+str(numero))
print("Número de veces q se repite en el archivo: "+str(con))
print("\n")


f=open("millon.txt","r")
tiempo3=time.time()
#Variable q hace la suma total
suma=0
#Contador
con=0
#Número aleatorio entre 1 y 4
numero=randint(1,4)
for x in f:
#If para si el número aleatorio coincide con alguno del archivo
#Int() convierte la x en un número entero para que pueda comparar
  if numero == int(x):
    #Si encuentra el contador cuenta uno y si encuentra mas #números
    con=con+1
  suma += int(x)
print("Millón de datos")
print("Suma = "+str(suma))
print("Duracion "+str(time.time()-tiempo3)+" segundos")
print("Número a validar: "+str(numero))
print("Número de veces q se repite en el archivo: "+str(con))
print("\n")


#3 Torre de hunai
print("torre de hunai")
def torre(discos, torreUno =1, torreTres =3):
    if discos:
        torre(discos-1,torreUno,6-torreUno-torreTres)
        print ("de disco "+ str(discos) + " de torre "+ str(torreUno) +" a la torre  "+ str(torreTres)) 
        torre(discos-1,6-torreUno-torreTres)
torre(discos=2)

#4 Algoritmo de búsqueda binaria recursiva

def binary_search_re(array, x, left, right):
    if left > right: # Llamada erronea
        return -1
    
    mid = (left+right)//2
    if array[mid] == x:# Caso base
        return mid
    elif array[mid] > x: # El numero esta a la izquierda
        return binary_search_re(array, x, left, mid-1)
    else: # El número esta a la derecha
        return binary_search_re(array, x, mid+1, right)

print("\n")
print("Resultado de búsqueda Binario")
arr = [0, 2, 3, 4, 5, 6, 7, 9, 10]
#arr es el array, 5 por ejemplo es el número que vamos a buscar, cero es pa posicicón inicla de array, len arr -1 es el final de array
print("El número esta en la siguiente posición del array: "
+str(binary_search_re(arr, 5, 0, len(arr)-1)))
