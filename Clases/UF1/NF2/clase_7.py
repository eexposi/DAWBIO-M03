""" CLASE 7 (28/10/22) - DICCIONARIOS ----------------------------------------------------------------------
# Un diccionario es un conjunto de pares de CLAVES y VALORES

# NORMAS:
    # - Cada clave debe ser ÚNICA.
    # - Una clave puede ser un tipo de dato (int,float,string...)
    # - Un diccionario no es una lista con posiciones. Básicamente los pares no están ordenados, por
    #   lo que no se pueden recorrer con índices.
    # - La función len() aplica también a los diccionarios. Retorna la cantidad de pares CLAVE-VALOR.
    # - No podemos encontrar la CLAVE a partir del valor, sólo el VALOR a partir de la CLAVE.

    # - La lista de pares se abre y cierra con llaves {}
                    RECORDATORIO:
                        - TUPLA ()
                        - LISTA []
    # - Cada par se separa por comas ","
    # - Entre CLAVE:VALOR usamos dos puntos ":"
----------------------------------------------------------------------------------------------------"""

""" DEFINICIÓN DE DICCIONARIOS ---------------------------------------------------------------------"""
dictionary = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
phone_numbers = {'jefe': 5551234567, 'Suzy': 22657854310}
empty_dictionary = {}

""" MUESTREO DE DICCIONARIOS -----------------------------------------------------------------------"""
# Mostrar diccionario completo
print(dictionary)
print(phone_numbers)
print(empty_dictionary)

# Mostrar el valor a partir de la CLAVE:
print(dictionary["gato"])
print(phone_numbers["jefe"])

for i in phone_numbers:  # El muestreo por índice sólo muestra las CLAVES
    print(i)

""" for e in range(len(phone_numbers)):     # El recorrido de los elementos NO FUNCIONA!
        print(phone_numbers[e])                                                             """

for clave in dictionary:
    print(clave, dictionary[clave], sep=' - ')  # Mostramos CLAVE --> VALOR

for trabajador, tlf in phone_numbers.items():  # Indicamos Alias para CLAVE y VALOR
    print(trabajador, "-->", tlf)

""" CAMBIO DE VALOR PARA UNA CLAVE CREADA ----------------------------------------------------------"""
dictionary["gato"] = "michu"
print(dictionary)

""" CREACIÓN DE UN NUEVO PAR DE DATOS --------------------------------------------------------------"""
dictionary["hormiga"] = "fourmi"
print(dictionary)

""" CREACIÓN DE UN DICCIONARIO DE LISTAS -----------------------------------------------------------"""
usuarios = {"nombres": [], "identificaciones": []}
nombre = ""
i = 0

# Leemos los datos y los agregamos a el diccionario
while nombre != "X":
    print("Ingrese los datos de la persona", i + 1)
    nombre = input("Nombre: ")
    identificacion = input("Identificación: ")

    # La primera lista es para los nombres
    usuarios["nombres"].append(nombre)

    # La segunda lista es para las identificaciones
    usuarios["identificaciones"].append(identificacion)
    i += 1

# Ahora mostremos los valores en el diccionario
for i in range(len(usuarios["nombres"]) - 1):
    print("Mostrando los datos de la persona", i + 1)
    print("Nombre:", usuarios["nombres"][i])
    print("Identificación:", usuarios["identificaciones"][i])

""" EJERCICIO 1 ------------------------------------------------------------------------------------
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está 
en el diccionario, pidiéndole que introduzca el símbolo si lo conoce. Finalmente mostrará toda la lista
en formato:

MONEDA <--> SÍMBOLO
-------------------
moneda 1 <--> símbolo 1
moneda 2 <--> símbolo 2
...
moneda nueva <--> símbolo nuevo
------------------------------------------------------------------------------------------------"""

""" EJERCICIO 2 -----------------------------------------------------------------------------------
Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe 
preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. 
Después se debe mostrar por pantalla la lista de la compra SIN EL PRECIO del artículo y el coste total, 
con el siguiente formato: 

LISTA DE LA COMPRA:
--------------------
Artículo 1
Artículo 2
Artículo ..
Artículo n
TOTAL   XXX €

Y finalmente, podemos pedirle el precio unitario de un artículo concreto, hasta que el usuario decida
terminar.                                                                                         """
