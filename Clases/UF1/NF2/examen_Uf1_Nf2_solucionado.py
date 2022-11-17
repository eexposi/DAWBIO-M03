"""EXAMEN NF2"""
""" 
EXAMEN NF2 - MATRICES, DICCIONARIOS Y CONTROL DE ERRORES --------------------------------------------

-----------------------------------------------------------
EJERCICIO 1  ----------------------------------------------
-----------------------------------------------------------
- Pedir al usuario su nombre y su DNI sin letra.
- Crear un diccionario con la key : nombre y el value : DNI con la letra.
- Mostrar todos los datos en forma de tabla.

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
# LETRAS = "TRWAGMYFPDXBNJZSQVHLCKE"
# dicc = {}
# todo_correcto = False
# while todo_correcto == False:
#     try:
#         nombre = input("Indicame tu nombre: ")
#         dni_sinletra = input("Indica el DNI sin letra: ")
#         if len(nombre) < 1:
#             raise Exception("El nombre es incorrecto.")
#         elif dni_sinletra[len(dni_sinletra)-1].isalpha():
#             raise Exception("Has puesto la letra, inútil")
#         elif len(dni_sinletra) != 8:
#             raise Exception("El DNI tiene una longitud incorrecta. Vigila que no hayas puesto la letra.")
#         else:
#             print("Los datos introducidos son correctos.")
#             todo_correcto = True
#     except Exception as error:
#         print(error)
#
# if todo_correcto == True:
#     todo_correcto = False
#     try:
#         letra = LETRAS[int(dni_sinletra)%23]
#         dni_completo = dni_sinletra + letra
#         dicc[nombre] = dni_completo
#         todo_correcto = True
#     except Exception as error:
#         print(error)
#
# if todo_correcto == True:
#     try:
#         for key in dicc:
#             print(key, dicc[key], sep = " ---- ")
#     except Exception as error:
#         print(error)


"""
-----------------------------------------------------------
EJERCICIO 2: CALCULADORA DE DIVISIÓN ----------------------
-----------------------------------------------------------
- Pedir al usuario 2 números.
- While hasta que le introduzcamos 'X' en el primer valor
- Realizar la división entre ellos, gestionando todos los posibles errores y mostrando por pantalla el error.
"""

"""
-----------------------------------------------------------
EJERCICIO 3: HUNDIR LA FLOTA ------------------------------
-----------------------------------------------------------
El código va a crear un tablero de 4x4 y va a colocar 2 barcos en él. El código debe permitir, fácilmente, cambiar
la posición de los barcos antes de lanzar el programa.

# Antes de empezar a jugar:
- Creamos un tablero de 4x4 vacío ('A')
- Colocamos 2 barcos (posición con 'B'), uno de 2 celdas y otro de 3 celdas (horizontal o vertical pero que no solapen)

# Al iniciar el programa...
- Mostrar el menú de juego (diccionario o lista) y tablero inicial con los barcos:
        1 - Jugar
        0 - Salir
- En random, hacemos tiradas:
    - devolver posición de la tirada
    - devolver agua (cambiar la casilla vacía 'A' por 'X') o tocado (cambiar la casilla de barco 'B' por 'T')
    - devolver estado del tablero
    - Esperar 'ENTER' para siguiente tirada
- Al completar 6 tiradas, deberemos devolver un mensaje según si hemos conseguido hundir todos los barcos o no


EJEMPLO DEL 1ER TURNO ----------------------------------------------------
-  Mostramos el tablero al empezar el juego:
           0 1 2 3
         0 A B B A
         1 A A A B
         2 A A A B
         3 A A A B

- Vemos las posiciones del disparo:
    Se dispara en la posicion x: 0 y: 1
    Tocado!

- Mostramos el tablero con las modificaciones:
           0 1 2 3
         0 A T B A
         1 A A A B
         2 A A A B
         3 A A A B
- Esperamos al siguiente turno:   "Pulsa ENTER para continuar..."

--------------------------------------------------------------------------------------------------- """
