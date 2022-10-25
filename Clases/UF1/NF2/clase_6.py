""" Clase 6: Contenedores de datos
Agrupan elementos/datos variados
(ARRAYS)
    - String: elementos ordenados, se pueden repetir
    - Lista: como string + son valores heterogeneos (incluso sublistas) y se pueden cambiar
    - Tupla: como las listas pero NO SE PUEDEN CAMBIAR
    - Matrices: estructuras de datos con filas y columnas (lista de listas)
    - Diccionario:
"""




""" MATRICES o TABLAS: lista de listas """
""" Recordar: tanto filas como columnas empiezan por el '0' """

M=[[],[]]
M=[[1,2],[3,4]]
print(M)
print(M[0])                     # Printamos la fila 0 [1,2]
print(M[1])                     # Printamos la fila 1 [3,4]
print(M[0][1])                  # Printamos la columna 1 de la fila 0 --> 2
print(M[1][0])                  # Printamos la columna 0 de la fila 1 --> 3


M2=[[1,2,3],[4,5,6,12],[7,8,9]]
print(M2[1])                    # Printamos la fila 1 [4,5,6]
print(M2[1][2])                 # Printamos la columna 2 de la fila 1 --> 6
print(len(M2))                  # ¿Cuántos valores tiene la matriz?

for i in range(0,3):              # Recorremos filas
    for j in range(0,3):          # Recorremos todas las columnas de cada fila
        print(M2[i][j])           # Printamos todos los valores
M2[1][1]=10                       # Modificamos el valor de la posición [1][1] --> Antes: 5

for i in range(0,3):              # Si no sabemos la posición de un valor concreto
    for j in range(0,3):          # Recorremos la matriz buscándolo, y si lo encontramos lo cambiamos
        if M2[i][j]==7:
            M2[i][j]=0            # Cambiamos el valor 7 por 0

for i in range(len(M2)):              # Podemos recorrer filas y columnas con len
    for j in range(len(M2[i])):       # Si el bucle interno coge el tamaño de las filas, podemos recorrer matrices heterogéneas (tamaño irregular)
        if M2[i][j]==7:
            M2[i][j]=0
        print(M2[i][j])


M3=[[1,"A", 0.5, "Eric"], [2, "B", 3.9, "Javi"], [3, "C", 100, "Pepe"]]
print(M3[1][3])                   # Printamos la columna 3 de la fila 1 --> Javi
print(M3[2][2])                   # Printamos la columna 2 de la fila 2 --> 100


M4=[[(1,2),(3,4),(5,6)],[(7,8),(9,10),(11,12)],[(13,14),(15,16),(17,18)]]
    # Estructura:
        # (1,2)    (3,4)    (5,6)
        # (7,8)    (9,10)   (11,12)
        # (13,14)  (15,16)  (17,18)

print(M4[2][1][0])              # Printamos la posición 0 de la columna 1 de la fila 2




""" EJERCICIO 1.1 ------------------------------------------------------------------------------ """
# 1) Mediante la siguiente matriz, generar un menú de opciones:
#    menu=[[1, "Opcion 1"], [2, "Opcion 2"], [3, "Opcion 3"], [4, "Salir"]]


""" EJERCICIO 1.2 ------------------------------------------------------------------------------ """
# Añadir una opción más al menú de opciones, pidiendo ambos datos al usuario.



""" EJERCICIO 2 ----------------------------------------------------------------------"""
# --- Menú ---
# 0 - Salir
# 1 - Jugar         # Otras opciones deben dar error y volver a mostrar el menú

# Crear manualmente una matriz tipo:
#    O   O   O
#    O   O   O
#    O   O   O

# Si elegimos la opción 1, nos pedirá 2 números independientes, es decir, 2 input (fila y columna). No aceptaremos posiciones incorrectas, volviendo a pedir el dato.
# Si la (fila,columna) contiene una 'O' --> cambiaremos la 'O' por 'X' y mostraremos la matriz con la nueva 'X'
# Cuando todas las posiciones de la matriz tengan 'X' --> mensaje de "WINNER"


""" EJERCICIO 2.2 --------------------------------------------------------------------"""
# Modifica el ejercicio 2.1 para que el sistema "juegue" de manera autónoma, es decir, sin pedirle
# valores de fila o columna al usuario.
#
# import random
# random.randint()
#


""" EJERCICIO 3 ---------------------------------------------------------------------"""
# 2) Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas
# con la siguiente forma: (nombre, DNI, destino). Ejemplo:
# [("Javier Carrasco", 39727461, "Tarragona"), ("Eric Exposito", 47766297, "Paris")]

# Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen.
# Ejemplo: [("Tarragona","Espanya"), ("Paris","Francia")]

# Hacer un menú iterativo, utilizando una tabla tipo [1, opcion 1], que permita al usuario realizar las siguientes operaciones:
#     3.1) Agregar pasajeros a la lista de viajeros
#     3.2) Agregar ciudades a la lista de ciudades
#     3.3) Dado el DNI de un pasajero, ver a qué ciudad viaja
#     3.4) Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad
#     3.5) Dado el DNI de un pasajero, ver a qué país viaja
#     3.6) Dado un país, mostrar cuántos pasajeros viajan a ese país
#     3.7) Salir del programa
# """