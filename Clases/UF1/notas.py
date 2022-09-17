# Clase 5
"""
Ordenar listas
"""

"""
OJO con la asignacion de listas
El programa:

Crea una lista de un elemento llamada lista1.
La asigna a una nueva lista llamada lista2.
Cambia el único elemento de lista1.
Imprime la lista2.
La parte sorprendente es el hecho de que el programa mostrará como resultado: 
[2], no [1], que parece ser la solución obvia.


Las listas (y muchas otras entidades complejas de Python) se almacenan de diferentes 
maneras que las variables ordinarias (escalares).

Se podría decir que:

El nombre de una variable ordinaria es el nombre de su contenido.
El nombre de una lista es el nombre de una ubicación de memoria donde se almacena la lista.
Lee estas dos líneas una vez más, la diferencia es esencial para comprender de que vamos a 
hablar a continuación.

La asignación: lista2 = lista1copia el nombre de la matriz, no su contenido. 
En efecto, los dos nombres (lista1 y lista2) identifican la misma ubicación en la
memoria de la computadora. Modificar uno de ellos afecta al otro, y viceversa."""

lista1 = ["a", "b", "c"]
lista2 = lista1
lista1[0] = "b"
print(lista2)

"""Copiar y crear nuevas listas
[:] Crea una lista nueva

# Copiando toda la lista
lista1 = [1]
lista2 = lista1[:]
lista1[0] = 2
print(lista2)

# Copiando parte de la lista
miLista = [10, 8, 6, 4, 2]
nuevaLista = miLista[1:3]
print(nuevaLista)

"""


"""in, not in de listas"""
miLista = [0, 3, 12, 8, 2]

print(5 in miLista)
print(5 not in miLista)
print(12 in miLista)



"""Ordenamiento burbuja

Se comparan los 2 primeros numeros y se ordenan.
Luego se comprueban los numeros 2 y 3 y se ordenan.
Sucesivamente hasta que no hayan mas cambios

CODIGO
"""
miLista = [8, 10, 6, 2, 4] # lista para ordenar
swapped = True # lo necesitamos verdadero (True) para ingresar al bucle while

while swapped:
    swapped = False # no hay swaps hasta ahora
    for i in range(len(miLista) - 1):
        if miLista[i] < miLista[i + 1]:
            swapped= True # ocurrió el intercambio!
            miLista[i], miLista[i + 1] = miLista[i + 1], miLista[i]

print(miLista)


"""Idea de ejercicio, borrar repetidos de una lista"""


"""Rellenar datos, comprension de listas y for"""
fila = ["PEON_BLANCO" for i in range(8)]
print(fila)

cuadrados = [x ** 2 for x in range(10)]
print(cuadrados)
