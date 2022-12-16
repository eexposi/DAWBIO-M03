"""
INSTRUCCIONES
- No se valorarán metodos/funciones de + 10 lineas.
- El programa principal podrá tener tambóen un máximo de
 10 lineas. Con excepción de encadenamientos de elif, que no contarán para este limite
-  Todos los metodos deberán estar comentados como se expuso en clase:
- Controlar los errores que se puedan producir FUERA de los metodos/funciones. El programa NO puede fallar.

def ejemplo(str):
#     '''
#     Esta funcion no hace nada
#     :param str: es un string que confrorma una palabra para nada
#     :return: el 1, porque funciona
#     '''
#     print("esto no hace nada")
#     return 1



"""
"""
EXAMEN UF2 - NF1 - METODOS Y FUNCIONES --------------------------------------------
"""

"""

"""

"""
(2P)
-----------------------------------------------------------
EJERCICIO 1  ----------------------------------------------
-----------------------------------------------------------
- Pedir al usuario su nombre y su DNI sin letra.
- Mostrar todos los datos en forma de tabla.
- Que el programa nos pida cuantos DNI queremos añadir
- 
                    Usuarios
                    ---------
                    Nombre --> XXXXXXXX-X

Las letras son: TRWAGMYFPDXBNJZSQVHLCKE
Y las letras se relacionan del 0 al 22:
0 = T
1 = R
2 = W
etc...

"""

"""
-----------------------------------------------------------
EJERCICIO 2  ----------------------------------------------
-----------------------------------------------------------
(4p)
Haremos un menu con las siguientes opciones: Salir, Crear BBDD, Crear 1 elemento BBDD 
Consultar toda la BBDD, Consultar 1 elemento BBDD, Eliminar elemento BBDD

base_datos = [
                ["ID", 
                "Nombre",
                "Telefono",
                "Fecha Nacimiento"]
                ]
                

- Crear BBDD: Generara un conjunto de datos para nuestra base de datos con 4 personas diferentes,
con 4 ID, 4 nombres...etc.
- Añadir 1 elemento: Pedir al usuario los datos y añadir un nuevo elemento a nuestra base de datos
- Consultar base de datos: Mostrar la base de datos en formato tabla:

BBDD
----
ID - Nombre - ...
ID - Nombre - ...

- Consultar un elemento: Pedir al usuario un ID, y mostrar todos sus datos:
ID: ----
Nombre: -----
...

- Eliminiar elemento: pedir un ID, mostrar los datos y solicitar confirmación del borrado.
ID: ----
Nombre: -----
...
Desea eliminiar el elemento?


"""

"""
-----------------------------------------------------------
EJERCICIO 3  ----------------------------------------------
-----------------------------------------------------------
(2p)

Completa el ejercicio adjunto, .py
Os dejamos la información.

PARTE 1:
- Haz que funcione el código, y se muestren los 3 prints con las 3 listas

PARTE 2:
- Haz que el codigo principal (sin contar las listas) sea de 1 linea

lst = ["Blanco", "Verde", "Amarillo", "Rojo", "Azul"]
lst2 = ["Blanco", "Negro", "Rojo", "Gris", "Naranja"]

def mostrar_lista(lst):
    for e in lst:
        print(e)

def get_coincidencias(lst, lst2):
    comparacion = []
    for i in lst:
        if lst[i] in lst2:
            comparacion.append(lst[i])
    return comparacion


mostrar_lista(lst[2])
print("LST2")
mostrar_lista(lst2)

lista_comparada = get_coincidencias(lst)
print("LST COMPARADA")
mostrar_lista(lista_comparada)



"""


"""
EJERCICIO 4
(2p)
Dadas las listas:
lst1 = [3, 8, 6, 5, 7, 7, 2, 7, 7, 10, 3, 4, 3, 1, 3, 6, 6, 5, 5, 6, 8, 3, 4, 8, 1, 10, 4, 9, 9, 7, 4, 10, 5, 0, 0, 2,
        0, 1, 5, 1, 2, 4, 4, 5, 3, 2, 6, 4, 10, 9, 4, 6, 2, 1, 3, 4, 7, 0, 2, 10, 5, 3, 1, 10, 6, 3, 7, 5, 5, 1, 5, 3,
        5, 9, 8, 0, 7, 6, 7, 2, 4, 4, 7, 8, 0, 1, 4, 3, 6, 2, 0, 10, 4, 10, 9, 3, 4, 4, 7, 5]
lst2 = [3, 1, 3, 6, 7, 0, 3, 9, 4, 5, 4, 2, 9, 2, 6, 5, 4, 2, 3, 9, 3, 4, 4, 1, 4, 10, 1, 6, 9, 1, 1, 2, 9, 3, 7, 7, 2,
        5, 1, 4, 7, 6, 10, 8, 6, 0, 8, 5, 6, 5, 3, 6, 3, 7, 9, 5, 6, 0, 8, 5, 10, 10, 4, 4, 3, 10, 5, 8, 2, 8, 9, 10, 2,
        0, 10, 7, 0, 1, 6, 2, 2, 7, 9, 5, 7, 6, 9, 2, 6, 1, 8, 0, 6, 3, 8, 1, 7, 2, 0]

4.1 - Compararemos ambas listas, mostrando por pantalla cuál de las 2 es mas larga.
4.2 - Realizaremos la media de cada una, indicando el resultado y cuál tiene la media más grande.
4.3 - Recorreremos la lista 1 y compararemos cada elemento de la lista, con el que tenga la misma posición de la otra.
 Indicando que lista posee el elemento con un valor más pequeño.
4.4 - Ordenaremos ambas listas de la misma forma y las mostraremos una de mayor a menor y la otra al revés de forma
invertida.
"""


