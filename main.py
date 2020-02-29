
#Primero y segundo programa

import time
from random import randint
listaUno=[];
listaDos=[];
listaTres=[];

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
  listaUno.append(int(x));
#If para si el número aleatorio coincide con alguno del archivo
#Int() convierte la x en un número entero para que pueda comparar
  if numero == int(x):
    #Si encuentra el contador cuenta uno y si encuentra mas #números
    con=con+1
  suma += int(x)
print("Ejercicio 1 y 2 archivo Mil datos")
print("Suma = "+str(suma))
print("Duración "+str(time.time()-tiempo)+" segundos")
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
  listaDos.append(int(x));
#If para si el número aleatorio coincide con alguno del archivo
#Int() convierte la x en un número entero para que pueda comparar
  if numero == int(x):
    #Si encuentra el contador cuenta uno y si encuentra mas #números
    con=con+1
  suma += int(x)
print("Ejercicio 1 y 2 archivo Diez mil datos")
print("Suma = "+str(suma))
print("Duración "+str(time.time()-tiempo2)+" segundos")
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
  listaTres.append(int(x));
 
#If para si el número aleatorio coincide con alguno del archivo
#Int() convierte la x en un número entero para que pueda comparar
  if numero == int(x):
    #Si encuentra el contador cuenta uno y si encuentra mas #números
    con=con+1
  suma += int(x)

print("Ejercicio 1 y 2 archivo Millón de datos")
print("Suma = "+str(suma))
print("Duración "+str(time.time()-tiempo3)+" segundos")
print("Número a validar: "+str(numero))
print("Número de veces q se repite en el archivo: "+str(con))
print("\n")


#3 Torre de hunai
print("Ejercico 3 Torre de hanói")
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
print("Ejercicio 4 resultado de búsqueda Binario")
arr = [0, 2, 3, 4, 5, 6, 7, 9, 10]
#arr es el array, 5 por ejemplo es el número que vamos a buscar, cero es pa posicicón inicla de array, len arr -1 es el final de array
print("El número esta en la siguiente posición del array: "
+str(binary_search_re(arr, 5, 0, len(arr)-1)))
print("\n")






















#lista Uno 

tiempoListaUno=time.time()
# Método de ordenamiento Burbuja
def ordenamientoBurbuja(unaLista):
  for numPasada in range(len(unaLista)-1,0,-1):
    for i in range(numPasada):
       if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp


ordenamientoBurbuja(listaUno)
print ("El orden en la lista por el método de la burbuja es:"+str(listaUno))
print("\n")
print("tiempo")
print("duracion "+str(time.time()-tiempoListaUno));
print("\n")
print("\n")


# Método de ordenamiento Inserción
tiempoListaUno=time.time()
def ordenamientoPorInsercion(unaLista):
   for indice in range(1,len(unaLista)):

     valorActual = unaLista[indice]
     posicion = indice

     while posicion>0 and unaLista[posicion-1]>valorActual:
         unaLista[posicion]=unaLista[posicion-1]
         posicion = posicion-1
     unaLista[posicion]=valorActual

ordenamientoPorInsercion(listaUno)
print("El orden en la lista por el método de inserción es:"+str(listaUno))
print("\n")
print("tiempo")
print("duracion "+str(time.time()-tiempoListaUno));
print("\n")
print("\n")

# Método de ordenamiento Quicksort
tiempoListaUno=time.time()
def sort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        #print(izquierda+["-"]+centro+["-"]+derecha)
        return sort(izquierda)+centro+sort(derecha)
    else:
      return lista

print()
print ("El orden en la lista por el método de Quicksort es:"+str(sort(listaUno)))
print("tiempo")
print("duracion "+str(time.time()-tiempoListaUno));
print("\n")
print("\n")


#lista Dos


# Método de ordenamiento Burbuja
tiempoListaUno=time.time()
def ordenamientoBurbuja(unaLista):
  for numPasada in range(len(unaLista)-1,0,-1):
    for i in range(numPasada):
       if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp


ordenamientoBurbuja(listaDos)
print ("El orden en la lista por el método de la burbuja es:"+str(listaDos))
print("\n")
print("tiempo")
print("duracion "+str(time.time()-tiempoListaUno));
print("\n")
print("\n")


# Método de ordenamiento Inserción
tiempoListaUno=time.time()
def ordenamientoPorInsercion(unaLista):
   for indice in range(1,len(unaLista)):

     valorActual = unaLista[indice]
     posicion = indice

     while posicion>0 and unaLista[posicion-1]>valorActual:
         unaLista[posicion]=unaLista[posicion-1]
         posicion = posicion-1
     unaLista[posicion]=valorActual

ordenamientoPorInsercion(listaDos)
print("El orden en la lista por el método de inserción es:"+str(listaDos))
print("\n")
print("tiempo")
print("duracion "+str(time.time()-tiempoListaUno));
print("\n")
print("\n")

# Método de ordenamiento Quicksort
tiempoListaUno=time.time()
def sort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        #print(izquierda+["-"]+centro+["-"]+derecha)
        return sort(izquierda)+centro+sort(derecha)
    else:
      return lista

print()
print ("El orden en la lista por el método de Quicksort es:"+str(sort(listaDos)))
print("tiempo")
print("duracion "+str(time.time()-tiempoListaUno));
print("\n")
print("\n")

#Lista Tres

# Método de ordenamiento Burbuja
tiempoListaUno=time.time()
def ordenamientoBurbuja(unaLista):
  for numPasada in range(len(unaLista)-1,0,-1):
    for i in range(numPasada):
       if unaLista[i]>unaLista[i+1]:
                temp = unaLista[i]
                unaLista[i] = unaLista[i+1]
                unaLista[i+1] = temp

ordenamientoBurbuja(listaTres)
print ("El orden en la lista por el método de la burbuja es:"+str(listaTres))
print("\n")
print("tiempo")
print("duracion "+str(time.time()-tiempoListaUno));
print("\n")
print("\n")

# Método de ordenamiento Inserción
tiempoListaUno=time.time()
def ordenamientoPorInsercion(unaLista):
   for indice in range(1,len(unaLista)):

     valorActual = unaLista[indice]
     posicion = indice

     while posicion>0 and unaLista[posicion-1]>valorActual:
         unaLista[posicion]=unaLista[posicion-1]
         posicion = posicion-1
     unaLista[posicion]=valorActual

ordenamientoPorInsercion(listaTres)
print("El orden en la lista por el método de inserción es:"+str(listaTres))
print("\n")
print("tiempo")
print("duracion "+str(time.time()-tiempoListaUno));
print("\n")
print("\n")

# Método de ordenamiento Quicksort
tiempoListaUno=time.time()
def sort(lista):
    izquierda = []
    centro = []
    derecha = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            elif i > pivote:
                derecha.append(i)
        #print(izquierda+["-"]+centro+["-"]+derecha)
        return sort(izquierda)+centro+sort(derecha)
    else:
      return lista

print()
print ("El orden en la lista por el método de Quicksort es:"+str(sort(listaTres)))
print("tiempo")
print("duracion "+str(time.time()-tiempoListaUno));
print("\n")
print("\n")
