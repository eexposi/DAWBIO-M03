"""CLASE 27 septiembre de 2022"""
"""
Asignación de listas
"""

lst1 = [1, 2, 3]
lst2 = lst1
print(lst1[1], lst2[1])
# Comprbamos como las listas estan enlazadas
"""
La asignación: lst2 = lista1copia el nombre de la matriz, no su contenido. 
En efecto, los dos nombres (lst1 y lst2) identifican la misma ubicación en la
memoria de la computadora. Modificar uno de ellos afecta al otro, y viceversa.
"""
lst1[1] = 99
print(lst1[1], lst2[1])

lst2[1] = 100
print(lst1[1], lst2[1])

"""Si queremos crear nuevas listas usamos:

[:]

Donde el elemento antes de los : y después son los elementos 
de inicio. Sin elementos, se cogeran todos

[:] == [0:len(lista]"""

lista = [1, 2, 3, 4, 5]
lista2 = lista[:]
print(lista2)
lista2 = lista[0:len(lista)]
print(lista2)

"""Tambien podemos usar [:] para crear listas filtrando
"""
lista2 = lista[2:4]
print(lista2)

import random

"""
Podemos simplificar la creación de listas
"""

fila = ["Hola" for i in range(8)]
print(fila)

cuadrados = [x ** 2 for x in range(10)]
print(cuadrados)

"""Funcion RANDOM"""
r1 = random.randint(0, 11)  # Numeros aleatorios entre el 0 y el 10

"""EJERCICIO 1 - Ordenamiento por burbuja"""
"""
NOTA: Se comparan los 2 primeros numeros y se ordenan.
Luego se comprueban los numeros 2 y 3 y se ordenan.
Sucesivamente hasta que no hayan mas cambios

Haremos un calculo de la campana de Gauss.
- Con la lista dada, ordenaremos los valores de menor a mayor
- Crearemos una nueva lista sin el primer y ultimo resultado
    Usar [:]
- Indicaremos cual es el valor medio (el que se encuentra en
la mitad, no la media).
- Buscaremos el valor mas repetido.
- Mostraremos todos los valores por debajo como Suspendidos
y por encima como aprobados.

lista_original = [0, 1, 3, 7, 9, 4, 5, 5, 5, 6, 9, 10, 10, 0, 3, 4, 5, 6]

SALIDA
Lista original
lista ordenada
Lista sin los numeros inicial/final
Valor medio
Valor mas repetido
"""
