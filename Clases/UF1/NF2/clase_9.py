""" CLASE 8 (15/11/22) -- REPASO FINAL PREVIO AL TEST DE LA UF1-NF2 """

""" EJERCICIO 1 (LISTAS) ---------------------------------------------------------------
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada 
asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar 
por pantalla las asignaturas que el usuario tiene que repetir.
"""

""" EJERCICIO 2 (DICCIONARIOS) ------------------------------------------------------------------
Escribir un programa que permita gestionar la base de datos de clientes de una empresa.
Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF,
y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono,
correo, preferente), donde preferente tendrá el valor True si se trata de un cliente
preferente. El programa debe preguntar al usuario por una opción del siguiente menú:
    (1) Añadir cliente,
    (2) Eliminar cliente,
    (3) Mostrar cliente,
    (4) Listar todos los clientes,
    (5) Listar clientes preferentes,
    (0) Terminar.
En función de la opción elegida el programa tendrá que hacer lo siguiente:

    1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
    2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
    3. Preguntar por el NIF del cliente y mostrar sus datos.
    4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
    5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
    0. Terminar el programa
"""

""" EJERCICIO 3 ----------------------------------------------------------------------------------
Escribir un programa que genere un diccionario con la información del directorio, donde cada
elemento corresponda a un cliente y tenga por clave su nif y por valor otro diccionario con
el resto de la información del cliente. Los diccionarios con la información de cada cliente
tendrán como claves los nombres de los campos y como valores la información de cada cliente
correspondientes a los campos. Es decir, un diccionario como el siguiente:

{'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 
               'teléfono': '656343576', 'descuento': 12.5}, 
 '71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 
               'teléfono': '692839321', 'descuento': 8.0}, 
 '63823376M': {'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 
               'teléfono': '664888233', 'descuento': 5.2}, 
 '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 
               'teléfono': '667677855', 'descuento': 15.7}}
"""
