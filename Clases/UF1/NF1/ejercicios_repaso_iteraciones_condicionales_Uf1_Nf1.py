"""Practicas clase preparación Pt1"""

"""EJERCICIO 1
- Solicitaremos al usuario un numero mayor que 1 y menor que 100. Este número serán los 
    bloques.
- Si el numero no cumple estos requisitos, volveremos a solicitarlo.
- Haremos una piramide usando el número de bloques como base.
- Tras mostrar la piramide, el programa nos indicará cuantos bloques se han utilizado.
- Ejemplo de piramide para 6 bloques:

*
**
***
****
*****

NOTA: No se podrán utilizar funciones, listas o métodos no explicados en clase
"""

NUM_BLOQUES = 6
bloques = NUM_BLOQUES

contador = 0
for i in range(NUM_BLOQUES):
    print("*" * i)
    contador += i
print("Bloques usados: " + str(contador))

"""
EJERCICIO 1.2
Mostrar la piramide anterior de forma inversa.
- Ejemplo:
******
*****
****
***
**
*
"""
contador = 0
for i in range(NUM_BLOQUES):
    print("*" * bloques)
    bloques -= 1
    contador += i
print("Bloques usados: " + str(contador))

"""Pedimos al usuario nombres constantemente y los guardamos en una lista. Dejaremos de pedir los nombres cuando 
el usuario introduzca un 0.
- Buscaremos el nombre mas largo, segun caracteres, y lo indicaremos.
- Buscaremos el mas corto, mostrandolo.
- Crearemos una nueva lista en la que no aparecerán los nombres que contengan una "a"
Ordenaremos los nombres en una nueva lista según la cantidad de caracteres de cada nombre. De menor a mayor
- Ejemplo:
Maria
Ant
"""

nombres = ["Eric", "Mariona", "Marc", "Maria"]
