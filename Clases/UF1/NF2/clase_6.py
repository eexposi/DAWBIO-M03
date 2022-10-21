""" Clase 6: Contenedores de datos
Agrupan elementos/datos variados
(ARRAYS)
    - String: elementos ordenados, se pueden repetir
    - Lista: como string + son valores heterogeneos (incluso sublistas) y se pueden cambiar
    - Tupla: como las listas pero NO SE PUEDEN CAMBIAR
    - Set (conjuntos):
    - Dictionary:
"""


"""LISTAS: como string + son valores heterogeneos (incluso sublistas) y se pueden cambiar """
lista_vacia = []
lista_vacia2 = list()
lista_con_elementos = [104, "hola", 0.8, True]
lista_desde_string = list("palabra")            # la lista contiene ["p","a","l","a","b","r","a"]
lista_desde_rango = list(range(5))              # la lista contiene [0,1,2,3,4]

print(str(lista_con_elementos[3]))
print(str(lista_desde_string[3]))
print(str(lista_desde_rango[3]))
print()

# Iteración por el índice (for y while)
for i in range(len(lista_con_elementos)):       # El FOR siempre incrementa la i
    print(i)
    print(lista_con_elementos[i])
print()

i=0                                             # + flexibilidad. Podemos incrementar la i cuando
while i<len(lista_con_elementos):               # nos interese
    print(lista_con_elementos[i])
    i+=1
print()

# Iteración por los elementos
for e in lista_con_elementos:                   # 'e' coge el valor que hay en la posición, no la
    print(e)                                    # posición en sí
print()

numeros = [1,2,3]
letras = ["A","B","C"]

combino = numeros+letras        # Se crea una lista de 6 elementos
print(combino)

combino2 = numeros+[letras]     # Se crea una lista de ...
print(combino2)
print(combino2[3])
print(combino2[3][1])

print(combino2[len(combino2)-1])        # Forma de acceder a la última posición de una lista

"""---------------------------------------------------------------------------- ¿QUÉ PODEMOS HACER CON LISTAS?
POSICIÓN DE UN ELEMENTO?: lista.index(elemento)
EXISTE UN ELEMENTO?: elemento in lista
CONTAR OCURRENCIAS: lista.count (elemento)

MODIFICAR ELEMENTO: lista[posicion] = nuevo_valor
AGREGAR ELEMENTO AL FINAL: lista.append(elemento)
AGREGAR ELEMENTO EN x POSICIÓN: lista.insert(pos,elemento)
ELIMINAR ELEMENTO: lista.remove(elemento)
VACIAR LISTA: lista.clear()
"""


"""TUPLAS: como las listas pero NO SE PUEDEN CAMBIAR"""
tupla_vacia = ()
tupla_vacia2 = tuple()
tupla_con_elementos = 104, "hola", 0.8, True     # paréntesis opcionales, comas obligatorias
tupla_desde_string = tuple("palabra")            # la lista contiene ["p","a","l","a","b","r","a"]
tupla_desde_rango = tuple(range(5))              # la lista contiene [0,1,2,3,4]

print(tupla_con_elementos)                       # Mostramos todos los elementos de la tupla
print(tupla_con_elementos[1])                    # Mostramos elemento [1]
print(tupla_con_elementos[1][1])                 # Si este elemento es parte de un array o lista, también podemos acceder a cada elemento de la misma
print()

tupla_string = ("palabra")                      # si no hay coma, esto es un simple string
print(type(tupla_string))                       # es de tipo string
print(tupla_string)
print(tupla_string[2])
print()

tupla_correcta = ("palabra",)                   # la tupla se crea cuando ponemos la coma, en este caso esta tupla sólo tiene un elemento
tupla_correcta2 = tuple("palabra")              # Esto también es una tupla, donde cada letra coge una posición
print(type(tupla_correcta))                     # Ambas son de tipo tupla
print(type(tupla_correcta))

print(tupla_correcta)
print(tupla_correcta[2])                        # ¿Qué se printará?
print(tupla_correcta2)
print(tupla_correcta2[2])
print()

tupla_final = (lista_con_elementos,"Agua")      # Creamos una tupla donde tenemos una lista en su primera posición
print(tupla_final)                              # Mostramos la tupla, con un elemento 'lista' y un string

lista_con_elementos.append(4)                   # Si añadimos un elemento a la lista
print(tupla_final)                              # la tupla recoge este cambio, pero realmente ella no cambia

#------------------------------------------------------------------------------------------------------------------------------------------------------------------
""" EJERCICIOS DE LISTAS """

""" ------------------------------------------------------------------------------- 
1) Dada la siguiente lista:
    L = ["almacenar", 8, "a", [1,2,3], True, (0,0,1), 85.7]

a) ¿Cuáles de estos elementos pertenecen a ella?
    85.7    0   True    [True]  [(0,0,1)]   85  "a" [1,2,3]
b) ¿Cómo obtener la posición en que se encuentra el elemento (0,0,1)?
c) ¿Cómo eliminar el último elemento, independientemente de cuántos elementos tenga la lista?
d) Utilizar una operación para contar cuántas veces aparece el string "a". ¿Cuál será el resultado?
"""

""" -------------------------------------------------------------------------------
2.1) 
Solicitar al usuario que introduzca números, los cuales se guardarán en una lista. Finalizar al
introducir el número 0, el cual no debe guardarse.

2.2)
A continuación, solicitar al usuario que introduzca un número y, si el número está en la lista,
eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar (no existe)

2.3)
Imprimir la SUMA de todos los números de la lista.

2.4) Solicitar al usuario otro número y crear una lista con los elementos de la lista original
que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.

2.5) Generar e imprimir una nueva lista que contenga como elementos a tuplas, cada una compuesta
por un número de la lista original y la cantidad de veces que aparece en ella. Por ejemplo,
si la lista original es [4,7,12,83,7,7,12,4], la nueva lista contendrá: [(4,2), (7,3), (12,2), (83,1)]
"""

""" ------------------------------------------------------------------------------
3) Escribir un programa que permita procesar datos de pasajeros de viaje en una lista de tuplas
con la siguiente forma: (nombre, DNI, destino). Ejemplo:
[("Javier Carrasco", 39727461, "Tarragona"), ("Eric Exposito", 47766297, "Paris")]

Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen.
Ejemplo: [("Tarragona","Espanya"), ("Paris","Francia")]

Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
    3.1) Agregar pasajeros a la lista de viajeros
    3.2) Agregar ciudades a la lista de ciudades
    3.3) Dado el DNI de un pasajero, ver a qué ciudad viaja
    3.4) Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad
    3.5) Dado el DNI de un pasajero, ver a qué país viaja
    3.6) Dado un país, mostrar cuántos pasajeros viajan a ese país
    3.7) Salir del programa
"""